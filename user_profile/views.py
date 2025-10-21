from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.decorators import login_required

@login_required
def create_profile(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        country = request.POST.get('country')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        
        bio = request.POST.get('bio')
        
        education_name = request.POST.get('education_name')
        education_field = request.POST.get('education_field')
        education_percentage = request.POST.get('education_percentage')

        skills = request.POST.get('skills')

        profile_picture = request.FILES.get('profile_picture')


        user_profile = UserProfile.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
            date_of_birth=date_of_birth,
            gender=gender,
            bio=bio,
            
            education_name=education_name,
            education_field=education_field,
            education_percentage=education_percentage,

            skills=skills,
            profile_picture=profile_picture
        )

        user_profile.save()

        # print(user_profile)

        return redirect('profile_view')

    
    return render(request, 'user_profile/profile_form.html')



@login_required
def edit_profile(request):

    if(not UserProfile.objects.filter(user=request.user).exists()):
        return redirect('create_profile')

    profile = UserProfile.objects.get(user=request.user)
    

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        country = request.POST.get('country')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        
        bio = request.POST.get('bio')
        
        education_name = request.POST.get('education_name')
        education_field = request.POST.get('education_field')
        education_percentage = request.POST.get('education_percentage')

        skills = request.POST.get('skills')

        profile_picture = request.FILES.get('profile_picture')


        print('Profile Picture', profile_picture)


            
        profile.user=request.user
            
        if first_name:
            profile.first_name=first_name
            
        if last_name: 
            profile.last_name=last_name
            
        if email:
            profile.email=email
            
        if phone_number:
            profile.phone_number=phone_number
            
        if address:
            profile.address=address
            
        if city:
            profile.city=city
            
        if state:
            profile.state=state
            
        if zip_code:
            profile.zip_code=zip_code
            
        if country:
            profile.country=country
            
        if date_of_birth:
            profile.date_of_birth=date_of_birth
            
        if gender:
            profile.gender=gender
            
        if bio:
            profile.bio=bio
            
        if education_name:
            profile.education_name=education_name
            
        if education_field:
            profile.education_field=education_field
            
        if education_percentage:
            profile.education_percentage=education_percentage
            
        if skills:
            profile.skills=skills
            
        if profile_picture:
            profile.profile_picture=profile_picture

        profile.save()

        return redirect('profile_view')



    return render(request, 'user_profile/profile_form.html', {'profile': profile})




@login_required
def profile_view(request):

    profile = UserProfile.objects.get(user=request.user)

    skills = profile.skills.split(',')

    for skill in skills:
        skill = skill.strip()

    profile.skills = skills


    return render(request, "user_profile/profile.html", {"profile": profile})


def not_found(request):
    return render(request, 'user_profile/not_found.html')




def landing(request):
    return render(request, 'user_profile/landing.html')
