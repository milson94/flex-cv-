<?php

namespace App\Http\Controllers;

use App\Models\User;
use App\Models\ReferenceCode;
use Illuminate\Http\Request;
use Illuminate\Support\Str;

class AdminController extends Controller
{
    // Middleware to ensure only admins can access these routes
    public function __construct()
    {
        $this->middleware('auth');
        $this->middleware('admin');
    }

    // View all users and their selected templates
    public function index()
    {
        $users = User::with('cv')->get();
        return view('admin.users', compact('users'));
    }

    // Generate a unique reference code for a user
    public function generateCode(Request $request, $userId)
    {
        $user = User::findOrFail($userId);

        // Generate a unique code
        $code = Str::random(10);

        // Save the code in the database
        ReferenceCode::create([
            'user_id' => $user->id,
            'code' => $code,
            'is_used' => false,
        ]);

        return redirect()->back()->with('success', 'Código gerado com sucesso: ' . $code);
    }

    // Validate a reference code and enable download for the user
    public function validateCode(Request $request)
    {
        $request->validate([
            'code' => 'required|string|exists:reference_codes,code',
        ]);

        $code = ReferenceCode::where('code', $request->code)->first();

        if ($code->is_used) {
            return redirect()->back()->with('error', 'Este código já foi usado.');
        }

        // Mark the code as used
        $code->update(['is_used' => true]);

        return redirect()->back()->with('success', 'Código validado com sucesso. O download foi ativado para o usuário.');
    }
}