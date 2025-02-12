@extends('layouts.app')

@section('content')
<div class="min-h-screen bg-gray-100 p-8">
    <div class="container mx-auto">
        <h1 class="text-3xl font-bold text-gray-800 mb-8">Escolha um Modelo de CV</h1>
        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-8">
            @php
                // Define template data
                $templates = [
                    ['image' => 'images/template1.png', 'title' => 'Modelo 1', 'description' => 'Design clássico e profissional.'],
                    ['image' => 'template2.png', 'title' => 'Modelo 2', 'description' => 'Design moderno e criativo.'],
                    ['image' => 'template3.png', 'title' => 'Modelo 3', 'description' => 'Design minimalista e elegante.'],
                    ['image' => 'template4.png', 'title' => 'Modelo 4', 'description' => 'Design moderno e profissional.'],
                    ['image' => 'template5.png', 'title' => 'Modelo 5', 'description' => 'Design clássico e minimalista.'],
                    ['image' => 'template6.png', 'title' => 'Modelo 6', 'description' => 'Design criativo e moderno.'],
                    ['image' => 'template7.png', 'title' => 'Modelo 7', 'description' => 'Design profissional e elegante.'],
                    ['image' => 'template8.png', 'title' => 'Modelo 8', 'description' => 'Design moderno e minimalista.'],
                    ['image' => 'template9.png', 'title' => 'Modelo 9', 'description' => 'Design clássico e criativo.'],
                    ['image' => 'template10.png', 'title' => 'Modelo 10', 'description' => 'Design elegante e profissional.'],
                    ['image' => 'template11.png', 'title' => 'Modelo 11', 'description' => 'Design moderno e profissional.'],
                    ['image' => 'template12.png', 'title' => 'Modelo 12', 'description' => 'Design clássico e minimalista.'],
                    ['image' => 'template13.png', 'title' => 'Modelo 13', 'description' => 'Design criativo e moderno.'],
                    ['image' => 'template14.png', 'title' => 'Modelo 14', 'description' => 'Design profissional e elegante.'],
                    ['image' => 'template15.png', 'title' => 'Modelo 15', 'description' => 'Design moderno e minimalista.'],
                    ['image' => 'template16.png', 'title' => 'Modelo 16', 'description' => 'Design clássico e criativo.'],
                    ['image' => 'template17.png', 'title' => 'Modelo 17', 'description' => 'Design elegante e profissional.'],
                    ['image' => 'template18.png', 'title' => 'Modelo 18', 'description' => 'Design moderno e profissional.'],
                    ['image' => 'template19.png', 'title' => 'Modelo 19', 'description' => 'Design clássico e minimalista.'],
                    ['image' => 'template20.png', 'title' => 'Modelo 20', 'description' => 'Design criativo e moderno.'],
                ];
            @endphp

            @foreach ($templates as $index => $template)
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <img src="{{ asset('images/' . $template['image']) }}" alt="{{ $template['title'] }}" class="w-full h-48 object-cover mb-4">
                    <h2 class="text-xl font-bold text-gray-800 mb-2">{{ $template['title'] }}</h2>
                    <p class="text-gray-600 mb-4">{{ $template['description'] }}</p>
                    <a href="{{ route('cv.download', ['template' => 'template' . ($index + 1)]) }}" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Escolher este Modelo</a>
                </div>
            @endforeach
        </div>
    </div>
</div>
@endsection