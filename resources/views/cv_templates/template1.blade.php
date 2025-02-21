<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            min-height: 100%;
            background: #fff;
            font-family: 'Roboto', sans-serif; /* Modern font: Roboto */
            font-weight: 400;
            color: #222;
            font-size: 10px; /* Reduced font size to fit on one page */
            line-height: 14px;
            padding: 0;
        }
        .cv-container {
            width: 100%;
            max-width: 800px; /* Adjusted to match a clean, single-page layout */
            margin: 0 auto;
            padding: 20px; /* Minimal padding for clean look */
            display: flex;
            justify-content: space-between;
        }
        .left-column, .right-column {
            width: 48%;
        }
        .title {
            text-align: left;
            font-size: 16px;
            font-style: italic; /* Slightly italicized title */
            margin-bottom: 10px;
            color: #555;
        }
        .header {
            margin-bottom: 15px;
            text-align: left; /* Changed from center to left alignment */
        }
        .header h1 {
            font-size: 24px;
            font-weight: bold;
            text-transform: uppercase;
            margin-bottom: 5px;
        }
        .role {
            font-size: 16px; /* Slightly larger for job position */
            color: #2c3e50; /* Subtle color for role */
            margin-bottom: 15px;
        }
        .contact-info, .summary, .section {
            margin-bottom: 15px;
        }
        .contact-info p, .summary p {
            margin: 3px 0;
            font-size: 10px;
            color: #555;
        }
        .section__title {
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 5px;
            text-transform: uppercase;
            color: #222;
        }
        .experience-item, .education-item, .reference-item {
            margin-bottom: 10px;
        }
        .experience-item h3, .education-item h3, .reference-item h3 {
            font-size: 12px;
            font-weight: bold;
            color: #222;
            margin: 0 0 5px 0;
        }
        .experience-item p, .education-item p, .reference-item p {
            margin: 2px 0;
            font-size: 10px;
            color: #555;
        }
        .skills-list, .languages-list {
            list-style: none;
            margin-bottom: 5px;
        }
        .skills-list li, .languages-list li {
            margin-bottom: 3px;
            font-size: 10px;
            color: #555;
        }
        .language-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 5px;
            font-size: 10px;
        }
        .language-table th, .language-table td {
            border: 1px solid #ddd;
            padding: 4px;
            text-align: left;
        }
        .language-table th {
            background-color: #f2f2f2;
        }
        .footer {
            text-align: center;
            font-size: 8px;
            color: #777;
            margin-top: 15px;
            border-top: 1px solid #ddd;
            padding-top: 10px;
            width: 100%; /* Span across both columns */
        }
    </style>
    <link href='https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap' rel='stylesheet' type='text/css'>
</head>
<body>
    <div class="cv-container">
        <!-- Left Column: Personal Data, Summary, Education -->
        <div class="left-column">
            <!-- Title -->
            <div class="title">Currículo Vitae</div>

            <!-- Header -->
            <div class="header">
                <h1>
                    <span class="first-name">{{ $first_name }}</span>
                    <span class="last-name">{{ $last_name }}</span>
                </h1>
                <p class="role">{{ $role }}</p>
            </div>

            <div class="contact-info">
                <p>{{ $email }} • {{ $linkedin }} • {{ $phone_number }}</p>
                <p>{{ $location }}</p>
                <p>Nacionalidade: {{ $nationality }}</p>
                <p>Data de Nascimento: {{ $date_of_birth }}</p>
                <p>Local de Nascimento: {{ $place_of_birth }}</p>
                <p>Gênero: {{ $gender == 'male' ? 'Masculino' : ($gender == 'female' ? 'Feminino' : 'Outro') }}</p>
            </div>

            <div class="section summary">
                <div class="section__title">Resumo</div>
                <p>{{ $summary }}</p>
            </div>

            <!-- Education -->
            <div class="section">
                <div class="section__title">Educação</div>
                @if (!empty($educations))
                    @foreach ($educations as $education)
                        <div class="education-item">
                            <h3>{{ $education['degree'] }} - {{ $education['school'] }}</h3>
                            <p><em>Ano de Conclusão: {{ $education['year_of_completion'] }}</em></p>
                        </div>
                    @endforeach
                @else
                    <p>Sem educação adicionada.</p>
                @endif
            </div>
        </div>

        <!-- Right Column: Skills, Languages, Experience, References, Additional Information -->
        <div class="right-column">
            <!-- Skills -->
            <div class="section">
                <div class="section__title">Habilidades</div>
                <ul class="skills-list">
                    @if (!empty($skills))
                        @foreach (is_array($skills) ? $skills : explode(',', $skills) as $skill)
                            <li>{{ trim($skill) }}</li>
                        @endforeach
                    @else
                        <p>Sem habilidades adicionadas.</p>
                    @endif
                </ul>
            </div>

            <!-- Languages -->
            <div class="section">
                <div class="section__title">Idiomas</div>
                @if (!empty($languages))
                    <table class="language-table">
                        <tr>
                            <th>Idioma</th>
                            <th>Conversação</th>
                            <th>Leitura</th>
                            <th>Escrita</th>
                        </tr>
                        @foreach ($languages as $language)
                            <tr>
                                <td>{{ $language['language'] }}</td>
                                <td>{{ $language['speaking_level'] == 'basic' ? 'Básico' : ($language['speaking_level'] == 'good' ? 'Bom' : 'Fluente') }}</td>
                                <td>{{ $language['reading_level'] == 'basic' ? 'Básico' : ($language['reading_level'] == 'good' ? 'Bom' : 'Fluente') }}</td>
                                <td>{{ $language['writing_level'] == 'basic' ? 'Básico' : ($language['writing_level'] == 'good' ? 'Bom' : 'Fluente') }}</td>
                            </tr>
                        @endforeach
                    </table>
                @else
                    <p>Sem idiomas adicionados.</p>
                @endif
            </div>

            <!-- Experience -->
            <div class="section">
                <div class="section__title">Experiência</div>
                @if (!empty($experiences))
                    @foreach ($experiences as $experience)
                        <div class="experience-item">
                            <h3>{{ $experience['title'] }} - {{ $experience['company_name'] }}</h3>
                            <p><em>{{ $experience['start_date'] }} - {{ $experience['end_date'] ?: 'Atual' }}</em></p>
                            @if (!empty($experience['company_description']))
                                <p>Descrição da Empresa: {{ $experience['company_description'] }}</p>
                            @endif
                            @if (!empty($experience['achievements']))
                                <p>Conquistas: {{ $experience['achievements'] }}</p>
                            @endif
                            @if (!empty($experience['duties']))
                                <p>Responsabilidades:</p>
                                <ul>
                                    @foreach (is_array($experience['duties']) ? $experience['duties'] : explode(',', $experience['duties']) as $duty)
                                        <li>{{ trim($duty) }}</li>
                                    @endforeach
                                </ul>
                            @endif
                        </div>
                    @endforeach
                @else
                    <p>Sem experiência adicionada.</p>
                @endif
            </div>

            <!-- References -->
            <div class="section">
                <div class="section__title">Referências</div>
                @if (!empty($references))
                    @foreach ($references as $reference)
                        <div class="reference-item">
                            <h3>{{ $reference['reference_name'] }}</h3>
                            <p>Cargo: {{ $reference['reference_position'] }}</p>
                            <p>Telefone: {{ $reference['reference_phone'] }}</p>
                        </div>
                    @endforeach
                @else
                    <p>Sem referências adicionadas.</p>
                @endif
            </div>

            <!-- Additional Information -->
            <div class="section">
                <div class="section__title">Informações Adicionais</div>
                @if (!empty($additional_information))
                    <ul>
                        @foreach ($additional_information as $info)
                            <li>{{ $info }}</li>
                        @endforeach
                    </ul>
                @else
                    <p>Sem informações adicionais.</p>
                @endif
            </div>
        </div>
    </div>
</body>
</html>