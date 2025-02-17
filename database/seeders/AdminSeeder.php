<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use App\Models\Admin;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class AdminSeeder extends Seeder
{
    public function run()
    {
        // Create the first admin user
        Admin::create([
            'name' => 'Admin Name',
            'email' => 'admin@example.com',
            'password' => Hash::make('password'), // Use a strong password!
        ]);

        // Create the second admin user
        Admin::create([
            'name' => 'Admin User 2',
            'email' => 'admin2@example.com',
            'password' => Hash::make('password123'), // Use a strong password!
        ]);

        // Create the third admin user
        Admin::create([
            'name' => 'Admin User 3',
            'email' => 'admin3@example.com',
            'password' => Hash::make('password321'), // Use a strong password!
        ]);

        // Create the fourth admin user with specific credentials
        Admin::create([
            'name' => 'Edmilson',
            'email' => 'mangueleedmilson@gmail.com',
            'password' => Hash::make('edmil94'), // Use a strong password!
        ]);
    }
}
