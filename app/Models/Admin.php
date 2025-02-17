<?php
namespace App\Models;

 use Illuminate\Database\Eloquent\Factories\HasFactory;
 use Illuminate\Database\Eloquent\Model;
 use Illuminate\Contracts\Auth\Authenticatable;
 use Illuminate\Auth\Authenticatable as AuthenticatableTrait;

 class Admin extends Model implements Authenticatable  //Important declaration
 {
    use AuthenticatableTrait;
    use HasFactory;

    protected $fillable = [
     'name',
     'email',
     'password',
     ];

    protected $hidden = [
     'password',
     'remember_token',
    ];
 }
