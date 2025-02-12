<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up()
    {
        Schema::create('c_v_s', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->onDelete('cascade');
            $table->string('first_name');
            $table->string('last_name');
            $table->string('role');
            $table->string('email');
            $table->string('linkedin')->nullable();
            $table->string('location')->nullable();
            $table->text('summary')->nullable();
            $table->string('company_name')->nullable();
            $table->string('title')->nullable();
            $table->text('company_description')->nullable();
            $table->text('achievements')->nullable();
            $table->string('school')->nullable();
            $table->string('degree')->nullable();
            $table->year('year_of_completion')->nullable();
            $table->text('skills')->nullable();
            $table->string('place_of_birth')->nullable();
            $table->string('nationality')->nullable();
            $table->string('phone_number')->nullable();
            $table->date('date_of_birth')->nullable();
            $table->string('gender')->nullable();
            $table->text('duties')->nullable();
            $table->date('start_date')->nullable();
            $table->date('end_date')->nullable();
            $table->boolean('current')->default(false);
            $table->json('languages')->nullable();
            $table->text('additional_information')->nullable();
            $table->json('references')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('c_v_s');
    }
};
