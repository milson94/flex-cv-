<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;


class CV extends Model
{
    use HasFactory;

    protected $fillable = [
        'name', 'role', 'email', 'linkedin', 'location', 'summary', 'skills'
    ];

    // Relationship with experiences
    public function experiences()
    {
        return $this->hasMany(Experience::class);
    }

    // Relationship with educations
    public function educations()
    {
        return $this->hasMany(Education::class);
    }
}