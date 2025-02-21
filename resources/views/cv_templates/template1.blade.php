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
            background: #eee;
            font-family: 'Lato', sans-serif;
            font-weight: 400;
            color: #222;
            font-size: 14px;
            line-height: 26px;
            padding-bottom: 50px;
        }
        .cv-container {
            max-width: 700px;
            background: #fff;
            margin: 50px auto 0px;
            box-shadow: 1px 1px 2px #DAD7D7;
            border-radius: 3px;
            padding: 40px;
        }
        .header {
            margin-bottom: 30px;
        }
        .header h1 {
            font-size: 40px;
            text-transform: uppercase;
            margin-bottom: 5px;
        }
        .header .first-name {
            font-weight: 700;
        }
        .header .last-name {
            font-weight: 300;
        }
        .contact-info {
            margin-bottom: 20px;
            background-color: #0073e6;
            padding: 15px;
            border-radius: 5px;
        }
        .contact-info p {
            margin: 3px 0;
            font-size: 16px;
            color: #fff;
            display: flex;
            align-items: center;
        }
        .contact-info i {
            margin-right: 5px;
            color: #fff;
        }
        .section {
            margin-bottom: 40px;
        }
        .section__title {
            letter-spacing: 2px;
            color: #54AFE4;
            font-weight: bold;
            margin-bottom: 10px;
            text-transform: uppercase;
        }
        .section p {
            margin: 5px 0;
            font-size: 16px;
            color: #555;
        }
        .experience-item, .education-item {
            margin-bottom: 20px;
        }
        .experience-item h3, .education-item h3 {
            font-size: 20px;
            color: #2c3e50;
            margin: 0;
        }
        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .skills span {
            background-color: #2c3e50;
            color: #fff;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 14px;
        }
        .language-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }
        .language-table th, .language-table td {
            border: 1px solid #ddd;
            padding: 8px;
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
        <!-- Header -->
        <div class="header">
            <h1>
                <span class="first-name">{{ $first_name }}</span>
                <span class="last-name">{{ $last_name }}</span>
            </h1>
            <p>{{ $role }}</p>
        </div>

        <!-- Contact Info -->
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

        <!-- Summary -->
        <div class="section">
            <div class="section__title">Resumo</div>
            <p>{{ $summary }}</p>
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

        <!-- Skills -->
        <div class="section">
            <div class="section__title">Habilidades</div>
            <div class="skills">
                @if (!empty($skills))
                    @foreach (is_array($skills) ? $skills : explode(',', $skills) as $skill)
                        <span>{{ trim($skill) }}</span>
                    @endforeach
                @else
                    <p>Sem habilidades adicionadas.</p>
                @endif
            </div>
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

        <!-- References -->
        <div class="section">
            <div class="section__title">Referências</div>
            @if (!empty($references))
                @foreach ($references as $reference)
                    <div class="experience-item">
                        <h3>{{ $reference['reference_name'] }}</h3>
                        <p>Cargo: {{ $reference['reference_position'] }}</p>
                        <p>Telefone: {{ $reference['reference_phone'] }}</p>
                    </div>
                @endforeach
            @else
                <p>Sem referências adicionadas.</p>
            @endif
        </div>
    </div>
</body>
</html>