@extends('layouts.app')

@section('content')
<div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
        <!-- Logo -->
        <div class="text-center mb-6">
            <h1 class="text-3xl font-bold text-blue-600">Flex Cv</h1>
            <p class="text-gray-600">Faça login para continuar</p>
        </div>

        <!-- Login Form -->
        <form method="POST" action="{{ route('login') }}">
            @csrf

            <!-- Email Input -->
            <div class="mb-4">
                <label for="email" class="block text-gray-700 text-sm font-bold mb-2">Endereço de Email</label>
                <input
                    type="email"
                    id="email"
                    name="email"
                    value="{{ old('email') }}"
                    required
                    autofocus
                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600 @error('email') border-red-500 @enderror"
                    placeholder="Digite seu email"
                >
                @error('email')
                    <p class="text-red-500 text-sm mt-1">{{ $message }}</p>
                @enderror
            </div>

            <!-- Password Input -->
            <div class="mb-6">
                <label for="password" class="block text-gray-700 text-sm font-bold mb-2">Senha</label>
                <input
                    type="password"
                    id="password"
                    name="password"
                    required
                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600 @error('password') border-red-500 @enderror"
                    placeholder="Digite sua senha"
                >
                @error('password')
                    <p class="text-red-500 text-sm mt-1">{{ $message }}</p>
                @enderror
            </div>

            <!-- Remember Me Checkbox -->
            <div class="mb-6">
                <label class="flex items-center">
                    <input
                        type="checkbox"
                        name="remember"
                        class="form-checkbox h-4 w-4 text-blue-600"
                        {{ old('remember') ? 'checked' : '' }}
                    >
                    <span class="ml-2 text-gray-700">Lembrar de mim</span>
                </label>
            </div>

            <!-- Login Button -->
            <div class="mb-6">
                <button
                    type="submit"
                    class="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600"
                >
                    Entrar
                </button>
            </div>

            <!-- Register Link -->
            <div class="text-center mb-4">  <!-- Added a margin-bottom for spacing -->
                <a href="{{ route('register') }}" class="text-blue-600 hover:underline">Não tem uma conta? Cadastre-se</a>
            </div>

            <!-- Forgot Password Link -->
            <div class="text-center">
                <a href="{{ route('password.request') }}" class="text-blue-600 hover:underline">Esqueceu sua senha?</a>
            </div>

            <!-- Google Login Button -->
            <div class="mt-6">
                <a
                    href="{{ route('google.login') }}"
                    class="w-full flex items-center justify-center bg-red-600 text-white py-2 px-4 rounded-lg hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-600"
                >
                    <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-1.25 17.292c-2.561 0-4.646-2.086-4.646-4.646s2.086-4.646 4.646-4.646c1.26 0 2.313.457 3.156 1.205l-1.29 1.29c-.352-.336-.805-.527-1.313-.527-1.105 0-2 .895-2 2s.895 2 2 2c1.105 0 2-.895 2-2h-2v-1.75h3.5c.138 0 .25.112.25.25v2.5c0 2.561-2.086 4.646-4.646 4.646zm6.5 0c-.69 0-1.25-.56-1.25-1.25v-2.5c0-.69.56-1.25 1.25-1.25s1.25.56 1.25 1.25v2.5c0 .69-.56 1.25-1.25 1.25z"/>
                    </svg>
                    Entrar com Google
                </a>
            </div>
        </form>
    </div>
</div>
@endsection