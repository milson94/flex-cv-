<?php

use App\Http\Controllers\Admin\AdminLoginController;
use App\Http\Controllers\AdminController;
use App\Http\Controllers\Auth\AuthenticatedSessionController;
use App\Http\Controllers\Auth\GoogleController;
use App\Http\Controllers\CVController;
use App\Http\Controllers\DashboardController;
use App\Http\Controllers\HomeController;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

// Authentication Routes
Auth::routes();
Route::get('/home', [HomeController::class, 'index'])->name('home');

// Logout Route (Moved Here for better organization)
Route::post('/logout', [AuthenticatedSessionController::class, 'destroy'])
    ->middleware('auth')
    ->name('logout');

// Google Authentication Routes
Route::get('/auth/google', [GoogleController::class, 'redirectToGoogle'])->name('google.login');
Route::get('/auth/google/callback', [GoogleController::class, 'handleGoogleCallback']);


// Admin Authentication Routes
Route::prefix('admin')->group(function () {
    Route::get('/login', [AdminLoginController::class, 'showLoginForm'])->name('admin.login');  // Corrected URL
    
    Route::post('/login', [AdminLoginController::class, 'login'])->name('admin.login.submit');

    Route::middleware(['auth:admin'])->group(function () {
        Route::get('/', [AdminController::class, 'index'])->name('admin.dashboard');
        Route::get('/dashboard', [AdminLoginController::class, 'login'])->name('admin.dashboard');
        Route::post('/logout', [AdminLoginController::class, 'logout'])->name('admin.logout'); //AdminLoginController
        // Add other admin routes here
    });
});

// CV Routes (User Authentication Required)
Route::middleware('auth')->group(function () {
    Route::post('/cv/store', [CVController::class, 'store'])->name('cv.store');
    Route::post('/cv/preview', [CVController::class, 'preview'])->name('cv.preview');
});

// CV Routes (No Authentication Required)
Route::get('/cv/templates', [CVController::class, 'templates'])->name('cv.templates');
Route::get('/cv/download/{template}', [CVController::class, 'download'])->name('cv.download');


// Dashboard Route (User Authentication Required)
Route::middleware('auth')->group(function () {
    Route::get('/dashboard', [DashboardController::class, 'index'])->name('dashboard');
});

