@extends('layouts.app')

@section('content')
<div class="flex min-h-screen bg-gray-100">
    <!-- Sidebar (Hidden on Mobile) -->
    <div class="w-64 bg-white shadow-lg hidden md:block">
        @include('partials.sidebar')
    </div>

    <!-- Main Content -->
    <div class="flex-1 p-8 overflow-y-auto">
        <h1 class="text-3xl font-bold text-gray-800 mb-8">Pré-visualização do CV</h1>

        <!-- Success Message -->
        @if (session('success'))
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded mb-6">
                {{ session('success') }}
            </div>
        @endif

        <!-- Error Messages -->
        @if ($errors->any())
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
                <ul>
                    @foreach ($errors->all() as $error)
                        <li>{{ $error }}</li>
                    @endforeach
                </ul>
            </div>
        @endif

        <!-- CV Preview Form -->
        <form method="POST" action="{{ route('cv.preview') }}" class="bg-white p-8 rounded-lg shadow-lg">
            @csrf

            <!-- Personal Details -->
            <div class="mb-8">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">Detalhes Pessoais</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label for="first_name" class="block text-gray-700 text-sm font-bold mb-2">Primeiro Nome</label>
                        <input
                            type="text"
                            id="first_name"
                            name="first_name"
                            required
                            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                            placeholder="Digite seu primeiro nome"
                            value="{{ old('first_name') }}"
                        >
                    </div>
                    <div>
                        <label for="last_name" class="block text-gray-700 text-sm font-bold mb-2">Sobrenome</label>
                        <input
                            type="text"
                            id="last_name"
                            name="last_name"
                            required
                            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                            placeholder="Digite seu sobrenome"
                            value="{{ old('last_name') }}"
                        >
                    </div>
                    <div>
                        <label for="role" class="block text-gray-700 text-sm font-bold mb-2">Cargo que está se candidatando</label>
                        <input
                            type="text"
                            id="role"
                            name="role"
                            required
                            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                            placeholder="Digite o cargo"
                            value="{{ old('role') }}"
                        >
                    </div>
                    <div>
                        <label for="email" class="block text-gray-700 text-sm font-bold mb-2">Email</label>
                        <input
                            type="email"
                            id="email"
                            name="email"
                            required
                            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                            placeholder="Digite seu email"
                            value="{{ old('email') }}"
                        >
                    </div>
                    <div>
                        <label for="linkedin" class="block text-gray-700 text-sm font-bold mb-2">LinkedIn/Portfólio</label>
                        <input
                            type="text"
                            id="linkedin"
                            name="linkedin"
                            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                            placeholder="Digite seu LinkedIn ou link do portfólio"
                            value="{{ old('linkedin') }}"
                        >
                    </div>
                    <div>
                        <label for="location" class="block text-gray-700 text-sm font-bold mb-2">Localização</label>
                        <input
                            type="text"
                            id="location"
                            name="location"
                            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                            placeholder="Digite sua localização"
                            value="{{ old('location') }}"
                        >
                    </div>
                    <div>
                        <label for="place_of_birth" class="block text-gray-700 text-sm font-bold mb-2">Local de Nascimento</label>
                        <input
                            type="text"
                            id="place_of_birth"
                            name="place_of_birth"
                            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                            placeholder="Digite seu local de nascimento"
                            value="{{ old('place_of_birth') }}"
                        >
                    </div>
                    <div>
                        <label for="nationality" class="block text-gray-700 text-sm font-bold mb-2">Nacionalidade</label>
                        <input
                            type="text"
                            id="nationality"
                            name="nationality"
                            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                            placeholder="Digite sua nacionalidade"
                            value="{{ old('nationality') }}"
                        >
                    </div>
                    <div>
                        <label for="phone_number" class="block text-gray-700 text-sm font-bold mb-2">Telefone</label>
                        <input
                            type="text"
                            id="phone_number"
                            name="phone_number"
                            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                            placeholder="Digite seu número de telefone"
                            value="{{ old('phone_number') }}"
                        >
                    </div>
                    <div>
                        <label for="date_of_birth" class="block text-gray-700 text-sm font-bold mb-2">Data de Nascimento</label>
                        <input
                            type="date"
                            id="date_of_birth"
                            name="date_of_birth"
                            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                            value="{{ old('date_of_birth') }}"
                        >
                    </div>
                    <div>
                        <label for="gender" class="block text-gray-700 text-sm font-bold mb-2">Gênero</label>
                        <select
                            id="gender"
                            name="gender"
                            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                        >
                            <option value="">Selecione</option>
                            <option value="male" {{ old('gender') == 'male' ? 'selected' : '' }}>Masculino</option>
                            <option value="female" {{ old('gender') == 'female' ? 'selected' : '' }}>Feminino</option>
                            <option value="other" {{ old('gender') == 'other' ? 'selected' : '' }}>Outro</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- Summary -->
            <div class="mb-8">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">Resumo</h2>
                <textarea
                    id="summary"
                    name="summary"
                    rows="4"
                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                    placeholder="Explique por que você é a pessoa ideal para o cargo"
                >{{ old('summary') }}</textarea>
            </div>

            <!-- Experience -->
            <div class="mb-8">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">Experiência</h2>
                <div id="experience-fields" class="space-y-6">
                    <!-- Initial Experience Field -->
                    <div class="bg-gray-50 p-6 rounded-lg experience-field">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label for="company_name[]" class="block text-gray-700 text-sm font-bold mb-2">Nome da Empresa</label>
                                <input
                                    type="text"
                                    name="company_name[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                    placeholder="Digite o nome da empresa"
                                    value="{{ old('company_name.0') }}"
                                >
                            </div>
                            <div>
                                <label for="title[]" class="block text-gray-700 text-sm font-bold mb-2">Cargo</label>
                                <input
                                    type="text"
                                    name="title[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                    placeholder="Digite seu cargo"
                                    value="{{ old('title.0') }}"
                                >
                            </div>
                            <div>
                                <label for="start_date[]" class="block text-gray-700 text-sm font-bold mb-2">Data de Início</label>
                                <input
                                    type="date"
                                    name="start_date[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                    value="{{ old('start_date.0') }}"
                                >
                            </div>
                            <div>
                                <label for="end_date[]" class="block text-gray-700 text-sm font-bold mb-2">Data de Término</label>
                                <input
                                    type="date"
                                    name="end_date[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                    value="{{ old('end_date.0') }}"
                                >
                            </div>
                            <div>
                                <label for="current[]" class="block text-gray-700 text-sm font-bold mb-2">Atual</label>
                                <input
                                    type="checkbox"
                                    name="current[]"
                                    class="px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                    {{ old('current.0') ? 'checked' : '' }}
                                >
                            </div>
                        </div>
                        <div class="mt-4">
                            <label for="company_description[]" class="block text-gray-700 text-sm font-bold mb-2">Descrição da Empresa</label>
                            <textarea
                                name="company_description[]"
                                rows="3"
                                class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                placeholder="Descreva a empresa"
                            >{{ old('company_description.0') }}</textarea>
                        </div>
                        <div class="mt-4">
                            <label for="achievements[]" class="block text-gray-700 text-sm font-bold mb-2">Principais Conquistas</label>
                            <textarea
                                name="achievements[]"
                                rows="3"
                                class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                placeholder="Descreva suas conquistas"
                            >{{ old('achievements.0') }}</textarea>
                        </div>
                        <div class="mt-4">
                            <label for="duties[]" class="block text-gray-700 text-sm font-bold mb-2">Principais Responsabilidades</label>
                            <div id="duties-fields" class="space-y-2">
                                <input
                                    type="text"
                                    name="duties[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                    placeholder="Digite uma responsabilidade"
                                    value="{{ old('duties.0') }}"
                                >
                            </div>
                            <div class="mt-2 flex justify-between">
                                <button
                                    type="button"
                                    class="bg-blue-600 text-white px-3 py-1 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600 add-duty text-sm"
                                >
                                    Adicionar Responsabilidade
                                </button>
                                <button
                                    type="button"
                                    class="bg-red-500 text-white px-3 py-1 rounded-lg hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 remove-field text-sm"
                                >
                                    Remover
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Add Experience Button -->
                <div class="mt-4 flex justify-between">
                    <button
                        type="button"
                        id="add-experience"
                        class="bg-blue-600 text-white px-3 py-1 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600 text-sm"
                    >
                        Adicionar Experiência
                    </button>
                    <button
                        type="button"
                        class="bg-red-500 text-white px-3 py-1 rounded-lg hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 remove-field text-sm"
                    >
                        Remover
                    </button>
                </div>
            </div>

            <!-- Education -->
            <div class="mb-8">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">Educação</h2>
                <div id="education-fields" class="space-y-6">
                    <!-- Initial Education Field -->
                    <div class="bg-gray-50 p-6 rounded-lg education-field">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label for="school[]" class="block text-gray-700 text-sm font-bold mb-2">Escola/Universidade</label>
                                <input
                                    type="text"
                                    name="school[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                    placeholder="Digite o nome da instituição"
                                    value="{{ old('school.0') }}"
                                >
                            </div>
                            <div>
                                <label for="degree[]" class="block text-gray-700 text-sm font-bold mb-2">Grau e Área de Estudo</label>
                                <input
                                    type="text"
                                    name="degree[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                    placeholder="Digite seu grau e área de estudo"
                                    value="{{ old('degree.0') }}"
                                >
                            </div>
                            <div>
                                <label for="year_of_completion[]" class="block text-gray-700 text-sm font-bold mb-2">Ano de Conclusão</label>
                                <select
                                    name="year_of_completion[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                >
                                    <option value="">Selecione</option>
                                    @for ($year = date('Y'); $year >= 1900; $year--)
                                        <option value="{{ $year }}" {{ old('year_of_completion.0') == $year ? 'selected' : '' }}>{{ $year }}</option>
                                    @endfor
                                </select>
                            </div>
                        </div>
                        <div class="mt-4 flex justify-between">
                            <button
                                type="button"
                                class="bg-blue-600 text-white px-3 py-1 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600 add-education text-sm"
                            >
                                Adicionar Educação
                            </button>
                            <button
                                type="button"
                                class="bg-red-500 text-white px-3 py-1 rounded-lg hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 remove-field text-sm"
                            >
                                Remover
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Languages -->
            <div class="mb-8">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">Idiomas</h2>
                <div id="language-fields" class="space-y-6">
                    <!-- Initial Language Field -->
                    <div class="bg-gray-50 p-6 rounded-lg language-field">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label for="language[]" class="block text-gray-700 text-sm font-bold mb-2">Idioma</label>
                                <input
                                    type="text"
                                    name="language[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                    placeholder="Digite o idioma"
                                    value="{{ old('language.0') }}"
                                >
                            </div>
                            <div>
                                <label for="speaking_level[]" class="block text-gray-700 text-sm font-bold mb-2">Nível de Conversação</label>
                                <select
                                    name="speaking_level[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                >
                                    <option value="">Selecione</option>
                                    <option value="basic" {{ old('speaking_level.0') == 'basic' ? 'selected' : '' }}>Básico</option>
                                    <option value="good" {{ old('speaking_level.0') == 'good' ? 'selected' : '' }}>Bom</option>
                                    <option value="fluent" {{ old('speaking_level.0') == 'fluent' ? 'selected' : '' }}>Fluente</option>
                                </select>
                            </div>
                            <div>
                                <label for="reading_level[]" class="block text-gray-700 text-sm font-bold mb-2">Nível de Leitura</label>
                                <select
                                    name="reading_level[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                >
                                    <option value="">Selecione</option>
                                    <option value="basic" {{ old('reading_level.0') == 'basic' ? 'selected' : '' }}>Básico</option>
                                    <option value="good" {{ old('reading_level.0') == 'good' ? 'selected' : '' }}>Bom</option>
                                    <option value="fluent" {{ old('reading_level.0') == 'fluent' ? 'selected' : '' }}>Fluente</option>
                                </select>
                            </div>
                            <div>
                                <label for="writing_level[]" class="block text-gray-700 text-sm font-bold mb-2">Nível de Escrita</label>
                                <select
                                    name="writing_level[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                >
                                    <option value="">Selecione</option>
                                    <option value="basic" {{ old('writing_level.0') == 'basic' ? 'selected' : '' }}>Básico</option>
                                    <option value="good" {{ old('writing_level.0') == 'good' ? 'selected' : '' }}>Bom</option>
                                    <option value="fluent" {{ old('writing_level.0') == 'fluent' ? 'selected' : '' }}>Fluente</option>
                                </select>
                            </div>
                        </div>
                        <div class="mt-4 flex justify-between">
                            <button
                                type="button"
                                class="bg-blue-600 text-white px-3 py-1 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600 add-language text-sm"
                            >
                                Adicionar Idioma
                            </button>
                            <button
                                type="button"
                                class="bg-red-500 text-white px-3 py-1 rounded-lg hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 remove-field text-sm"
                            >
                                Remover
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Additional Information -->
            <div class="mb-8">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">Informações Adicionais</h2>
                <div id="additional-info-fields" class="space-y-2">
                    <input
                        type="text"
                        name="additional_information[]"
                        class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                        placeholder="Digite uma informação adicional"
                        value="{{ old('additional_information.0') }}"
                    >
                </div>
                <div class="mt-2 flex justify-between">
                    <button
                        type="button"
                        class="bg-blue-600 text-white px-3 py-1 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600 add-additional-info text-sm"
                    >
                        Adicionar Informação Adicional
                    </button>
                    <button
                        type="button"
                        class="bg-red-500 text-white px-3 py-1 rounded-lg hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 remove-field text-sm"
                    >
                        Remover
                    </button>
                </div>
            </div>

            <!-- References -->
            <div class="mb-8">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">Referências</h2>
                <div id="reference-fields" class="space-y-6">
                    <!-- Initial Reference Field -->
                    <div class="bg-gray-50 p-6 rounded-lg reference-field">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label for="reference_name[]" class="block text-gray-700 text-sm font-bold mb-2">Nome</label>
                                <input
                                    type="text"
                                    name="reference_name[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                    placeholder="Digite o nome da referência"
                                    value="{{ old('reference_name.0') }}"
                                >
                            </div>
                            <div>
                                <label for="reference_position[]" class="block text-gray-700 text-sm font-bold mb-2">Cargo</label>
                                <input
                                    type="text"
                                    name="reference_position[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                    placeholder="Digite o cargo da referência"
                                    value="{{ old('reference_position.0') }}"
                                >
                            </div>
                            <div>
                                <label for="reference_phone[]" class="block text-gray-700 text-sm font-bold mb-2">Telefone</label>
                                <input
                                    type="text"
                                    name="reference_phone[]"
                                    class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                                    placeholder="Digite o telefone da referência"
                                    value="{{ old('reference_phone.0') }}"
                                >
                            </div>
                        </div>
                        <div class="mt-4 flex justify-between">
                            <button
                                type="button"
                                class="bg-blue-600 text-white px-3 py-1 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600 add-reference text-sm"
                            >
                                Adicionar Referência
                            </button>
                            <button
                                type="button"
                                class="bg-red-500 text-white px-3 py-1 rounded-lg hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 remove-field text-sm"
                            >
                                Remover
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Skills -->
            <div class="mb-8">
                <h2 class="text-2xl font-bold text-gray-800 mb-4">Habilidades</h2>
                <div class="bg-gray-50 p-6 rounded-lg">
                    <textarea
                        id="skills"
                        name="skills"
                        rows="3"
                        class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                        placeholder="Liste suas habilidades"
                    >{{ old('skills') }}</textarea>
                </div>
            </div>

            <!-- Submit Button -->
            <div class="mt-8">
                <button
                    type="submit"
                    class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500"
                >
                    Escolher Modelo de CV
                </button>
            </div>
        </form>
    </div>
</div>

<script>
    // JavaScript to handle adding and removing new experience, education, language, additional info, reference fields, and duties
    document.getElementById('add-experience').addEventListener('click', function() {
        const experienceFields = document.getElementById('experience-fields');
        const newExperienceField = document.querySelector('.experience-field').cloneNode(true);
        newExperienceField.querySelectorAll('input, textarea, select').forEach(element => {
            element.value = '';
        });
        // Clear duties fields in the new experience
        newExperienceField.querySelector('#duties-fields').innerHTML = `
            <input type="text" name="duties[]" class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600" placeholder="Digite uma responsabilidade" value="">
        `;
        // Update button classes for new field
        newExperienceField.querySelector('.add-duty').classList.add('text-sm');
        newExperienceField.querySelector('.remove-field').classList.add('text-sm');
        experienceFields.appendChild(newExperienceField);
    });

    document.querySelectorAll('.add-education').forEach(button => {
        button.addEventListener('click', function() {
            const educationFields = document.getElementById('education-fields');
            const newEducationField = document.querySelector('.education-field').cloneNode(true);
            newEducationField.querySelectorAll('input, select').forEach(element => {
                element.value = '';
            });
            // Update button classes for new field
            newEducationField.querySelector('.add-education').classList.add('text-sm');
            newEducationField.querySelector('.remove-field').classList.add('text-sm');
            educationFields.appendChild(newEducationField);
        });
    });

    document.querySelectorAll('.add-language').forEach(button => {
        button.addEventListener('click', function() {
            const languageFields = document.getElementById('language-fields');
            const newLanguageField = document.querySelector('.language-field').cloneNode(true);
            newLanguageField.querySelectorAll('input, select').forEach(element => {
                element.value = '';
            });
            // Update button classes for new field
            newLanguageField.querySelector('.add-language').classList.add('text-sm');
            newLanguageField.querySelector('.remove-field').classList.add('text-sm');
            languageFields.appendChild(newLanguageField);
        });
    });

    document.querySelectorAll('.add-additional-info').forEach(button => {
        button.addEventListener('click', function() {
            const additionalInfoFields = document.getElementById('additional-info-fields');
            const newAdditionalInfoField = additionalInfoFields.querySelector('input').cloneNode(true);
            newAdditionalInfoField.value = '';
            additionalInfoFields.appendChild(newAdditionalInfoField);
        });
    });

    document.querySelectorAll('.add-reference').forEach(button => {
        button.addEventListener('click', function() {
            const referenceFields = document.getElementById('reference-fields');
            const newReferenceField = document.querySelector('.reference-field').cloneNode(true);
            newReferenceField.querySelectorAll('input').forEach(element => {
                element.value = '';
            });
            // Update button classes for new field
            newReferenceField.querySelector('.add-reference').classList.add('text-sm');
            newReferenceField.querySelector('.remove-field').classList.add('text-sm');
            referenceFields.appendChild(newReferenceField);
        });
    });

    document.querySelectorAll('.add-duty').forEach(button => {
        button.addEventListener('click', function() {
            const dutiesFields = button.parentElement.querySelector('#duties-fields');
            const newDutyField = dutiesFields.querySelector('input').cloneNode(true);
            newDutyField.value = '';
            dutiesFields.appendChild(newDutyField);
        });
    });

    // JavaScript to handle removing fields
    document.querySelectorAll('.remove-field').forEach(button => {
        button.addEventListener('click', function() {
            const parentField = button.closest('.experience-field, .education-field, .language-field, .reference-field');
            if (parentField) {
                parentField.remove();
            } else {
                // For additional info or duties, remove the specific input
                const input = button.closest('input');
                if (input) {
                    input.remove();
                }
            }
        });
    });
</script>
@endsection