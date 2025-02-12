@extends('layouts.app')

@section('content')
    <div class="flex items-center justify-center h-screen">
        <h1 class="text-4xl font-bold">Bem-vindo, {{ Auth::user()->name }}!</h1>
    </div>
@endsection