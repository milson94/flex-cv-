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
        html {
            height: 100%;
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
        .section:last-of-type {
            margin-bottom: 0px;
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
        .experience-item p, .education-item p {
            margin: 5px 0;
            color: #555;
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
    </style>
    <link href='https://fonts.googleapis.com/css?family=Lato:400,300,700' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" integrity="sha512-9usAa10IRO0HhonpyAIVpjrylPvoDwiPUiKdWk5t3PyolY1cOd4DSE0Ga+ri4AuTroPR5aQvXU9xC6qOPnzFeg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
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
        </div>

        <!-- Summary -->
        <div class="section">
            <div class="section__title">Summary</div>
            <p>{{ $summary }}</p>
        </div>

        <!-- Experience -->
        <div class="section">
            <div class="section__title">Experience</div>
            @if (!empty($experiences))
                @foreach ($experiences as $experience)
                    <div class="experience-item">
                        <h3>{{ $experience['title'] }} - {{ $experience['company_name'] }}</h3>
                        <p><em>{{ $experience['start_date'] }} - {{ $experience['end_date'] ?: 'Present' }}</em></p>
                        <p>{{ $experience['company_description'] }}</p>
                        <ul>
                            @foreach (explode(',', $experience['duties']) as $duty)
                                <li>{{ trim($duty) }}</li>
                            @endforeach
                        </ul>
                    </div>
                @endforeach
            @else
                <p>No experience added.</p>
            @endif
        </div>

        <!-- Education -->
        <div class="section">
            <div class="section__title">Education</div>
            @if (!empty($educations))
                @foreach ($educations as $education)
                    <div class="education-item">
                        <h3>{{ $education['degree'] }} - {{ $education['school'] }}</h3>
                        <p><em>Year of Completion: {{ $education['year_of_completion'] }}</em></p>
                    </div>
                @endforeach
            @else
                <p>No education added.</p>
            @endif
        </div>

        <!-- Skills -->
        <div class="section">
            <div class="section__title">Skills</div>
            <div class="skills">
                @if (!empty($skills))
                    @foreach (explode(',', $skills) as $skill)
                        <span>{{ trim($skill) }}</span>
                    @endforeach
                @else
                    <p>No skills added.</p>
                @endif
            </div>
        </div>
    </div>
</body>
</html>
