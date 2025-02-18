<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Barryvdh\DomPDF\Facade\Pdf;
use App\Models\CV; // Assuming you have a CV model

class CVController extends Controller
{
    public function download($template)
    {
        // Retrieve CV data from session
        $sessionData = session('cv_data');

        // Retrieve CV data from the database (if available)
        $cv = CV::where('user_id', auth()->id())->latest()->first();

        // If CV exists in the database, fetch experiences and educations
        if ($cv) {
            $experiences = $cv->experiences;
            $educations = $cv->educations;
            $languages = $cv->languages;
            $additional_information = $cv->additional_information;
            $references = $cv->references;
        } else {
            // Fallback to session data if no CV is found in the database
            $experiences = $sessionData['experiences'] ?? [];
            $educations = $sessionData['educations'] ?? [];
            $languages = $sessionData['languages'] ?? [];
            $additional_information = $sessionData['additional_information'] ?? [];
            $references = $sessionData['references'] ?? [];
        }

        // Prepare data for the template
        $data = [
            'first_name' => $sessionData['first_name'],
            'last_name' => $sessionData['last_name'],
            'role' => $sessionData['role'],
            'email' => $sessionData['email'],
            'linkedin' => $sessionData['linkedin'],
            'location' => $sessionData['location'],
            'summary' => $sessionData['summary'],
            'place_of_birth' => $sessionData['place_of_birth'],
            'nationality' => $sessionData['nationality'],
            'phone_number' => $sessionData['phone_number'],
            'date_of_birth' => $sessionData['date_of_birth'],
            'gender' => $sessionData['gender'],
            'skills' => $sessionData['skills'],
            'experiences' => $experiences,
            'educations' => $educations,
            'languages' => $languages,
            'additional_information' => $additional_information,
            'references' => $references,
        ];

        // Load the selected template
        $pdf = Pdf::loadView("cv_templates.$template", $data);

        // Download the PDF
        return $pdf->download('cv.pdf');
    }

    public function preview(Request $request)
{
    // Store CV data in session
    $cvData = [
        'first_name' => $request->input('first_name'),
        'last_name' => $request->input('last_name'),
        'role' => $request->input('role'),
        'email' => $request->input('email'),
        'linkedin' => $request->input('linkedin'),
        'location' => $request->input('location'),
        'summary' => $request->input('summary'),
        'place_of_birth' => $request->input('place_of_birth'),
        'nationality' => $request->input('nationality'),
        'phone_number' => $request->input('phone_number'),
        'date_of_birth' => $request->input('date_of_birth'),
        'gender' => $request->input('gender'),
        'skills' => $request->input('skills'),
    ];

    // Experience
    $companyNames = $request->input('company_name');
    $titles = $request->input('title');
    $descriptions = $request->input('company_description');
    $achievements = $request->input('achievements');
    $duties = $request->input('duties');
    $startDates = $request->input('start_date');
    $endDates = $request->input('end_date');
    $currentStatuses = $request->input('current');

    if (is_array($companyNames) && is_array($titles) && is_array($descriptions) && is_array($achievements) && is_array($duties) && is_array($startDates) && is_array($endDates) && is_array($currentStatuses) &&
        count($companyNames) == count($titles) && count($companyNames) == count($descriptions) &&
        count($companyNames) == count($achievements) && count($companyNames) == count($duties) &&
        count($companyNames) == count($startDates) && count($companyNames) == count($endDates) &&
        count($companyNames) == count($currentStatuses)) {
        $cvData['experiences'] = array_map(function ($company, $title, $description, $achievement, $duty, $startDate, $endDate, $current) {
            return [
                'company_name' => $company,
                'title' => $title,
                'company_description' => $description,
                'achievements' => $achievement,
                'duties' => $duty,
                'start_date' => $startDate,
                'end_date' => $endDate,
                'current' => $current,
            ];
        }, $companyNames, $titles, $descriptions, $achievements, $duties, $startDates, $endDates, $currentStatuses);
    } else {
        $cvData['experiences'] = [];
    }

    // Education
    $schools = $request->input('school');
    $degrees = $request->input('degree');
    $completionYears = $request->input('year_of_completion');

    if (is_array($schools) && is_array($degrees) && is_array($completionYears) &&
        count($schools) == count($degrees) && count($schools) == count($completionYears)) {
        $cvData['educations'] = array_map(function ($school, $degree, $completionYear) {
            return [
                'school' => $school,
                'degree' => $degree,
                'year_of_completion' => $completionYear,
            ];
        }, $schools, $degrees, $completionYears);
    } else {
        $cvData['educations'] = [];
    }

    $cvData['languages'] = $this->formatLanguages($request->all());
    $cvData['additional_information'] = $request->input('additional_information');
    $cvData['references'] = $this->formatReferences($request->all());

    $request->session()->put('cv_data', $cvData);

    // Redirect to template selection page
    return redirect()->route('cv.templates');
}

    public function templates()
    {
        return view('cv_templates');
    }

    public function store(Request $request)
    {
        // Validate the form data
        $validatedData = $request->validate([
            'first_name' => 'required|string|max:255',
            'last_name' => 'required|string|max:255',
            'role' => 'required|string|max:255',
            'email' => 'required|email|max:255',
            'linkedin' => 'nullable|url|max:255',
            'location' => 'nullable|string|max:255',
            'summary' => 'nullable|string',
            'place_of_birth' => 'nullable|string|max:255',
            'nationality' => 'nullable|string|max:255',
            'phone_number' => 'nullable|string|max:20',
            'date_of_birth' => 'nullable|date',
            'gender' => 'nullable|string|max:10',
            'company_name' => 'nullable|array',
            'title' => 'nullable|array',
            'company_description' => 'nullable|array',
            'achievements' => 'nullable|array',
            'duties' => 'nullable|array',
            'start_date' => 'nullable|array',
            'end_date' => 'nullable|array',
            'current' => 'nullable|array',
            'school' => 'nullable|array',
            'degree' => 'nullable|array',
            'year_of_completion' => 'nullable|array',
            'language' => 'nullable|array',
            'speaking_level' => 'nullable|array',
            'reading_level' => 'nullable|array',
            'writing_level' => 'nullable|array',
            'additional_information' => 'nullable|array',
            'reference_name' => 'nullable|array',
            'reference_position' => 'nullable|array',
            'reference_phone' => 'nullable|array',
            'skills' => 'nullable|string',
        ]);

        // Save the CV data to the database
        $cv = CV::create([
            'user_id' => auth()->id(),
            'first_name' => $validatedData['first_name'],
            'last_name' => $validatedData['last_name'],
            'role' => $validatedData['role'],
            'email' => $validatedData['email'],
            'linkedin' => $validatedData['linkedin'],
            'location' => $validatedData['location'],
            'summary' => $validatedData['summary'],
            'place_of_birth' => $validatedData['place_of_birth'],
            'nationality' => $validatedData['nationality'],
            'phone_number' => $validatedData['phone_number'],
            'date_of_birth' => $validatedData['date_of_birth'],
            'gender' => $validatedData['gender'],
            'skills' => $validatedData['skills'],
            'languages' => $this->formatLanguages($validatedData),
            'additional_information' => $validatedData['additional_information'],
            'references' => $this->formatReferences($validatedData),
        ]);

        // Save Experience
        if (!empty($validatedData['company_name'])) {
            foreach ($validatedData['company_name'] as $index => $companyName) {
                $cv->experiences()->create([
                    'company_name' => $companyName,
                    'title' => $validatedData['title'][$index],
                    'company_description' => $validatedData['company_description'][$index],
                    'achievements' => $validatedData['achievements'][$index],
                    'duties' => $validatedData['duties'][$index],
                    'start_date' => $validatedData['start_date'][$index],
                    'end_date' => $validatedData['end_date'][$index],
                    'current' => $validatedData['current'][$index] ?? false,
                ]);
            }
        }

        // Save Education
        if (!empty($validatedData['school'])) {
            foreach ($validatedData['school'] as $index => $school) {
                $cv->educations()->create([
                    'school' => $school,
                    'degree' => $validatedData['degree'][$index],
                    'year_of_completion' => $validatedData['year_of_completion'][$index],
                ]);
            }
        }

        // Redirect back with a success message
        return redirect()->back()->with('success', 'CV salvo com sucesso!');
    }

    private function formatLanguages($data)
    {
        $languages = [];
        if (!empty($data['language'])) {
            foreach ($data['language'] as $index => $language) {
                $languages[] = [
                    'language' => $language,
                    'speaking_level' => $data['speaking_level'][$index],
                    'reading_level' => $data['reading_level'][$index],
                    'writing_level' => $data['writing_level'][$index],
                ];
            }
        }
        return $languages;
    }

    private function formatReferences($data)
    {
        $references = [];
        if (!empty($data['reference_name'])) {
            foreach ($data['reference_name'] as $index => $name) {
                $references[] = [
                    'name' => $name,
                    'position' => $data['reference_position'][$index],
                    'phone' => $data['reference_phone'][$index],
                ];
            }
        }
        return $references;
    }
}
