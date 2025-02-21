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
            font-family: 'Lato', sans-serif;
            font-weight: 400;
            color: #222;
            font-size: 12px;
            line-height: 16px;
            padding: 0;
        }
        .cv-container {
            width: 100%;
            max-width: 1000px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            border: 1px solid #ddd;
        }
        .left-column, .right-column {
            width: 48%;
            padding: 20px; /* Basic, even padding for both columns */
        }
        .header {
            margin-bottom: 10px;
        }
        .header h1 {
            font-size: 24px;
            text-transform: uppercase;
            margin-bottom: 5px;
        }
        .header .first-name {
            font-weight: 700;
        }
        .header .last-name {
            font-weight: 300;
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
            font-size: 12px;
            color: #555;
        }
        .section__title {
            letter-spacing: 1px;
            color: #54AFE4;
            font-weight: bold;
            margin-bottom: 5px;
            text-transform: uppercase;
            font-size: 14px;
        }
        .experience-item, .education-item, .reference-item {
            margin-bottom: 10px;
        }
        .experience-item h3, .education-item h3, .reference-item h3 {
            font-size: 14px;
            color: #2c3e50;
            margin: 0;
        }
        .skills-list {
            list-style: none; /* Remove bullet points */
        }
        .skills-list li {
            margin-bottom: 5px; /* Each skill on its own line */
            color: #555;
            font-size: 12px;
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
    </style>
    <link href='https://fonts.googleapis.com/css?family=Lato:400,300,700' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"/>
</head>
<body>
    <div class="cv-container">
        <!-- Left Column: Personal Information -->
        <div class="left-column">
            <div class="header">
                <h1>
                    <span class="first-name">{{ $first_name }}</span>
                    <span class="last-name">{{ $last_name }}</span>
                </h1>
                <p class="role">{{ $role }}</p>
            </div>

            <div class="contact-info">
                <p><i class="fas fa-phone"></i> {{ $phone_number }}</p>
                <p><i class="fas fa-envelope"></i> {{ $email }}</p>
                <p><i class="fab fa-linkedin"></i> {{ $linkedin }}</p>
                <p><i class="fas fa-map-marker-alt"></i> {{ $location }}</p>
                <p><i class="fas fa-globe"></i> Nacionalidade: {{ $nationality }}</p>
                <p><i class="fas fa-birthday-cake"></i> Data de Nascimento: {{ $date_of_birth }}</p>
                <p><i class="fas fa-map-pin"></i> Local de Nascimento: {{ $place_of_birth }}</p>
                <p><i class="fas fa-venus-mars"></i> Gênero: {{ $gender == 'male' ? 'Masculino' : ($gender == 'female' ? 'Feminino' : 'Outro') }}</p>
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

            <!-- Skills (each on its own line, no background) -->
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
        </div>

        <!-- Right Column: Professional Information -->
        <div class="right-column">
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