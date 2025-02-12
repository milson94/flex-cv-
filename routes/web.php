<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Auth\GoogleController;
use App\Http\Controllers\DashboardController;
use App\Http\Controllers\CVController;
use App\Http\Controllers\Auth\LoginController;

Route::get('/', function () {
    return view('welcome');
});

Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');

Route::middleware('admin')->group(function () {
    Route::get('/admin', [AdminController::class, 'index']);
});

// Logout Route
Route::post('/logout', [AuthenticatedSessionController::class, 'destroy'])
    ->middleware('auth')
    ->name('logout');




// Google Authentication Routes
Route::get('/auth/google', [GoogleController::class, 'redirectToGoogle'])->name('google.login');
Route::get('/auth/google/callback', [GoogleController::class, 'handleGoogleCallback']);


Route::post('/cv/preview', [CVController::class, 'preview'])->name('cv.preview');

Route::get('/cv/templates', [CVController::class, 'templates'])->name('cv.templates');
Route::get('/cv/download/{template}', [CVController::class, 'download'])->name('cv.download');

Route::middleware('auth')->group(function () {
    Route::post('/cv/store', [CVController::class, 'store'])->name('cv.store');
});

Route::middleware('auth')->group(function () {
    Route::get('/dashboard', [DashboardController::class, 'index'])->name('dashboard');
});
