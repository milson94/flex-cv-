@extends('layouts.app')

@section('content')
<div class="container mx-auto px-6 py-8">
    <h1 class="text-3xl font-bold mb-8">Painel de Administração</h1>

    <div class="bg-white shadow rounded-lg p-6">
        <h2 class="text-2xl font-bold mb-6">Lista de Usuários</h2>

        <table class="min-w-full bg-white">
            <thead>
                <tr>
                    <th class="py-2">Nome</th>
                    <th class="py-2">Email</th>
                    <th class="py-2">Modelo Escolhido</th>
                    <th class="py-2">Ações</th>
                </tr>
            </thead>
            <tbody>
                @foreach ($users as $user)
                    <tr class="border-b">
                        <td class="py-4">{{ $user->name }}</td>
                        <td class="py-4">{{ $user->email }}</td>
                        <td class="py-4">{{ $user->cv->template ?? 'Nenhum' }}</td>
                        <td class="py-4">
                            <a href="{{ route('admin.generate.code', $user->id) }}" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">Gerar Código</a>
                        </td>
                    </tr>
                @endforeach
            </tbody>
        </table>
    </div>

    <div class="bg-white shadow rounded-lg p-6 mt-8">
        <h2 class="text-2xl font-bold mb-6">Validar Código</h2>
        <form action="{{ route('admin.validate.code') }}" method="POST">
            @csrf
            <div class="flex items-center">
                <input type="text" name="code" class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600" placeholder="Insira o código" required>
                <button type="submit" class="bg-green-600 text-white px-6 py-2 rounded-lg hover:bg-green-700 ml-4">Validar</button>
            </div>
        </form>
    </div>
</div>
@endsection