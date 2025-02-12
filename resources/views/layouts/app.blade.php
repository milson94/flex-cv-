<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flex CV - Construtor de CVs</title>
    <!-- Link to the CSS file in the public/css directory -->
    <link href="{{ asset('css/styles.css') }}" rel="stylesheet">
    <!-- Tailwind CSS -->
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <style>
        /* Custom styles for mobile menu */
        .mobile-menu {
            display: none;
        }
        .mobile-menu.active {
            display: block;
        }

        /* Sticky footer styles */
        body {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        .content {
            flex: 1;
        }

        /* Ensure form and button are vertically centered */
        .nav-form {
            display: flex;
            align-items: center;
        }
    </style>
</head>
<body class="bg-gray-100">
    <!-- Header -->
    <header class="bg-white shadow">
        <div class="container mx-auto px-6 py-4 flex justify-between items-center">
            <!-- Logo as a clickable link -->
            <a href="{{ route('home') }}" class="flex items-center">
                <img src="{{ asset('images/logo.png') }}" alt="Flex CV Logo" class="h-10 w-auto mr-2">
            </a>
            <!-- Desktop Navigation -->
            <nav class="hidden md:flex space-x-4 items-center">
                <a href="#" class="text-gray-700 hover:text-blue-600">Blog</a>
                <a href="#" class="text-gray-700 hover:text-blue-600">Preços</a>
                <a href="#" class="text-gray-700 hover:text-blue-600">Para Organizações</a>
                @if (Auth::check())
                    <form method="POST" action="{{ route('logout') }}" onsubmit="return confirm('Tem certeza que deseja sair?');" class="nav-form">
                        @csrf
                        <button type="submit" class="text-gray-700 hover:text-blue-600">Sair</button>
                    </form>
                @else
                    <a href="{{ route('login') }}" class="text-gray-700 hover:text-blue-600">Entrar</a>
                @endif
                <a href="{{ route('login') }}" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">Começar</a>
            </nav>
            <!-- Mobile Burger Button -->
            <button id="mobile-menu-button" class="md:hidden focus:outline-none">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
                </svg>
            </button>
        </div>
        <!-- Mobile Navigation Menu -->
        <div id="mobile-menu" class="mobile-menu md:hidden bg-white">
            <a href="#" class="block px-4 py-2 text-gray-700 hover:bg-blue-600 hover:text-white">Blog</a>
            <a href="#" class="block px-4 py-2 text-gray-700 hover:bg-blue-600 hover:text-white">Preços</a>
            <a href="#" class="block px-4 py-2 text-gray-700 hover:bg-blue-600 hover:text-white">Para Organizações</a>
            @if (Auth::check())
                <form method="POST" action="{{ route('logout') }}" onsubmit="return confirm('Tem certeza que deseja sair?');" class="block px-4 py-2">
                    @csrf
                    <button type="submit" class="text-gray-700 hover:text-blue-600">Sair</button>
                </form>
            @else
                <a href="{{ route('login') }}" class="block px-4 py-2 text-gray-700 hover:bg-blue-600 hover:text-white">Entrar</a>
            @endif
            <a href="{{ route('login') }}" class="block px-4 py-2 bg-blue-600 text-white hover:bg-blue-700">Começar</a>
        </div>
    </header>

    <!-- Main Content -->
    <main class="content">
        @yield('content')  <!-- This is where the content of individual pages will be injected -->
    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white py-8">
        <div class="container mx-auto px-6">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div>
                    <!-- White logo in the footer -->
                    <a href="{{ route('home') }}" class="flex items-center">
                        <img src="{{ asset('images/logo-white.png') }}" alt="Flex CV Logo" class="h-10 w-auto mr-2">
                    </a>
                    <p class="text-gray-400 mt-2">Construtor de CVs profissional para ajudá-lo a alcançar seus objetivos de carreira.</p>
                </div>
                <div>
                    <h3 class="text-lg font-bold mb-4">Links Rápidos</h3>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-white">Blog</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Preços</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">Para Organizações</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-lg font-bold mb-4">Contacto</h3>
                    <p class="text-gray-400">Email: suporte@flexcv.com</p>
                    <p class="text-gray-400">Telefone: +258 84 123 4567</p>
                </div>
            </div>
        </div>
    </footer>

    <!-- JavaScript to toggle mobile menu -->
    <script>
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');

        mobileMenuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('active');
        });

        // Add More Experience
        document.getElementById('add-experience').addEventListener('click', function () {
            const experienceFields = document.getElementById('experience-fields');
            const newExperienceField = document.querySelector('.experience-field').cloneNode(true);

            // Clear input values in the new field
            newExperienceField.querySelectorAll('input, textarea').forEach(input => {
                input.value = '';
            });

            experienceFields.appendChild(newExperienceField);
        });

        // Add More Education
        document.getElementById('add-education').addEventListener('click', function () {
            const educationFields = document.getElementById('education-fields');
            const newEducationField = document.querySelector('.education-field').cloneNode(true);

            // Clear input values in the new field
            newEducationField.querySelectorAll('input, textarea').forEach(input => {
                input.value = '';
            });

            educationFields.appendChild(newEducationField);
        });
    </script>
</body>
</html>