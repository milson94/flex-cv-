@extends('layouts.app')

@section('content')
    <!-- Hero Section -->
    <section class="bg-blue-600 text-white py-20">
        <div class="container mx-auto px-6 text-center">
            <h1 class="hero-text text-4xl font-bold mb-4">Construtor de CVs que ajuda você a ser contratado nas melhores empresas</h1>
            <p class="mb-8">Escolha um modelo de CV e crie o seu CV em minutos.</p>
            <div class="space-x-4">
                <a href="{{ route('home') }}" class="bg-white text-blue-600 px-8 py-3 rounded-full font-semibold hover:bg-gray-100">Criar CV</a>
                <a href="{{ route('register') }}" class="bg-green-500 text-white px-8 py-3 rounded-full font-semibold hover:bg-green-600">Registrar</a>
            </div>
        </div>
    </section>

    <!-- Slider Section -->
    <section class="container mx-auto px-6 py-12">
        <h2 class="text-3xl font-bold text-center mb-8">Escolha um Modelo de CV</h2>
        <div class="slider">
            <!-- Slider Items -->
            @for ($i = 1; $i <= 20; $i++)
                <div class="slider-item {{ $i > 6 ? 'hidden' : '' }}">
                    <a href="{{ route('home') }}">
                        <img src="{{ asset("images/templates/template{$i}.png") }}" alt="Template {{ $i }}">
                    </a>
                </div>
            @endfor
        </div>
        <button id="show-more" class="show-more-btn">Mostrar Mais ↓</button>
        <button id="show-less" class="show-less-btn hidden">Mostrar Menos ↑</button>
    </section>

    <!-- Features Section -->
    <section class="feature-section py-16">
        <div class="container mx-auto px-6">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-gray-800">CVs profissionais compatíveis com ATS</h2>
                <p class="text-gray-600">Mude a fonte, cor e combinações de fundo.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="bg-white p-6 rounded-lg shadow">
                    <h3 class="text-xl font-bold mb-4">Layouts personalizados</h3>
                    <p class="text-gray-600">Escolha entre layouts de uma coluna, duas colunas ou várias páginas.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow">
                    <h3 class="text-xl font-bold mb-4">Adaptação ao emprego</h3>
                    <p class="text-gray-600">Analise as habilidades e experiências necessárias para o emprego que deseja.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow">
                    <h3 class="text-xl font-bold mb-4">Lista de verificação</h3>
                    <p class="text-gray-600">Receba uma lista de ações para melhorar o seu CV.</p>
                </div>
            </div>
        </div>
    </section>
@endsection

<!-- Include CSS -->
<link rel="stylesheet" href="{{ asset('css/styles.css') }}">

<!-- Include JavaScript -->
<script src="{{ asset('js/scripts.js') }}" defer></script>
