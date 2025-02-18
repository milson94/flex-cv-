@extends('layouts.app')

@section('content')
<div class="min-h-screen bg-gray-100 p-8">
    <div class="container mx-auto">
        <h1 class="text-3xl font-bold text-gray-800 mb-8">Escolha um Modelo de CV</h1>
        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-8">
            @if(count($templates) > 0)
                @foreach ($templates as $templateName)
                    @php
                        // Generate template data based on templateName
                        $templateNumber = str_replace('template', '', $templateName); // Extract the number
                        $templateImage = 'template' . $templateNumber . '.png'; // Image name
                        $templateTitle = 'Modelo ' . $templateNumber; // Title
                        $templateDescription = 'Descrição do modelo ' . $templateNumber; // Default description
                    @endphp

                    <div class="bg-white p-6 rounded-lg shadow-lg">
                        <img src="{{ asset('images/' . $templateImage) }}" alt="{{ $templateTitle }}" class="w-full h-48 object-cover mb-4">
                        <h2 class="text-xl font-bold text-gray-800 mb-2">{{ $templateTitle }}</h2>
                        <p class="text-gray-600 mb-4">{{ $templateDescription }}</p>
                        <a href="{{ route('cv.download', ['template' => $templateName]) }}" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Escolher este Modelo</a>
                    </div>
                @endforeach
            @else
                <p>Nenhum template encontrado.</p>
            @endif
        </div>
    </div>
</div>
@endsection