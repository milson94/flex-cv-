<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV</title>
    <style>
        body {
          font-family: sans-serif;
          margin: 0;
          padding: 0;
          display: flex;
        }

        .left-column {
          background-color: #6aa3a3;
          color: white;
          width: 35%;
          padding: 20px;
          box-sizing: border-box;
        }

        .right-column {
          width: 65%;
          padding: 20px;
          box-sizing: border-box;
        }

        h1 {
          margin-bottom: 5px;
          font-size: 2.5em;
        }

        h2 {
          margin-top: 20px;
          margin-bottom: 10px;
          font-size: 1.5em;
          color: #333;
        }

        h3 {
          margin-bottom: 5px;
          font-size: 1.2em;
          color: #555;
        }

        p {
          margin-bottom: 10px;
          line-height: 1.4;
        }

        .section-title {
          font-size: 1.3em;
          font-weight: bold;
          margin-bottom: 10px;
        }

        .contact-info {
          margin-top: 20px;
          background-color: #0073e6;
          padding: 15px;
          border-radius: 5px;
        }

        .contact-info p {
          margin-bottom: 5px;
          font-size: 16px;
          color: #fff;
          display: flex;
          align-items: center;
        }

        .reference {
          margin-top: 20px;
        }

        .reference h3 {
          margin-bottom: 2px;
        }

        .education-item,
        .experience-item {
          margin-bottom: 15px;
        }

        .skills-list {
          list-style: none;
          padding: 0;
        }

        .skills-list li {
          margin-bottom: 5px;
        }

         .experience-details {
           display: flex;
           flex-direction: column;
        }

        .experience-details .job-title {
            margin-bottom: 3px;
            font-weight: bold;
        }

        .experience-details .company-name {
            font-style: italic;
            color: #555;
        }

        .experience-details .date-range {
            font-size: 0.9em;
            color: #777;
            margin-bottom: 5px;
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


@media print {
  body {
    font-size: 12pt; /* Adjust font size for printing */
  }
  .left-column {
    background-color: #6aa3a3 !important; /* Ensure background color is printed */
    color: white !important;
  }
  .contact-info {
    background-color: #0073e6 !important; /* Ensure background color is printed */
    color: white !important;
  }
}

    </style>
    <link href='https://fonts.googleapis.com/css?family=Lato:400,300,700' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" integrity="sha512-9usAa10IRO0HhonpyAIVpjrylPvoDwiPUiKdWk5t3PyolY1cOd4DSE0Ga+ri4AuTroPR5aQvXU9xC6qOPnzFeg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>
    <div class="cv-container">

        <div class="left-column">
            <img src="image_placeholder.jpg" alt="Profile Image" class="profile-image">
            <div class="contact-info">
                <p><i class="fas fa-phone"></i> {{ $phone_number }}</p>
                <p><i class="fas fa-envelope"></i> {{ $email }}</p>
                <p><i class="fab fa-linkedin"></i> {{ $linkedin }}</p>
                <p><i class="fas fa-map-marker-alt"></i> {{ $location }}</p>
            </div>
        </div>

        <div class="right-column">

            <div class="header">
                <h1>
                    <span class="first-name">{{ $first_name }}</span>
                    <span class="last-name">{{ $last_name }}</span>
                </h1>
                <p>{{ $role }}</p>
            </div>

            <div class="section">
                <h2 class="section-title">Summary</h2>
                <p>{{ $summary }}</p>
            </div>

            <div class="section">
                <h2 class="section-title">Experience</h2>
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

            <div class="section">
                <h2 class="section-title">Education</h2>
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

            <div class="section">
                <h2 class="section-title">Skills</h2>
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

    </div>
</body>
</html>