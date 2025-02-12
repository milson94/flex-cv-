<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Education extends Model
{
    use HasFactory;

    protected $fillable = [
        'cv_id', 'school', 'degree'
    ];

    // Relationship with CV
    public function cv()
    {
        return $this->belongsTo(CV::class);
    }
}
