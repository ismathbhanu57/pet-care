from itertools import chain

from django.db.models import Q, Count
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html", {})


def blog(request):
    return render(request, "blog.html", {})


def blog_details(request):
    return render(request, "blog_details.html", {})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, "contact.html", {"msg": "Successfully Saved"})
        return render(request, "contact.html", {})
    return render(request, "contact.html", {})


def services(request):
    return render(request, "services.html", {})


def customer_home(request):
    return render(request, "customer_home.html", {})

def customer_login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        if Customer.objects.filter(email=email).exists():
            user = Customer.objects.get(email=email)
            if user is not None:
                pwd = user.password
                if password == pwd:
                    if user.status == "Accepted":
                        request.session["email"] = email
                        return render(request, 'customer_home.html', {})
                    else:
                        return render(request, "customer_login.html", {"msg": "Account Is On Hold"})
                else:
                    return render(request, "customer_login.html", {"msg": "Wrong Passwords"})
            else:
                return render(request, "customer_login.html", {"msg": ""})
        return render(request, "customer_login.html", {"msg": "Email Not Registered"})
    return render(request, "customer_login.html", {})

def customer_register(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES)
        email = request.POST['email']
        if form.is_valid():
            email=form.cleaned_data["email"]
            if Customer.objects.filter(email=email).exists():
                return render(request, 'customer_registration.html', {"msg": "This Email is Already Exists"})
            else:
                form.is_valid()
                form.save()
                return render(request, 'customer_login.html', {"msg": "Successfully Register"})
        else:
            return render(request, 'customer_registration.html', {"msg": "Invalid Data"})
    else:
        form = CustomerForm()
        return render(request, 'customer_registration.html', {"form":form})


def customer_logout(request):
    request.session.flush()
    return redirect('/customer_login')



def admin_home(request):
    return render(request, "admin_home.html", {})


def admin_login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        login = Admin.objects.filter(email=email, password=password)
        if login.exists():
            request.session['email'] = email
            return render(request, 'admin_home.html', {})
        else:
            return render(request, "admin_login.html", {"msg": "Invalid Creditinals"})
    return render(request, 'admin_login.html', {})


def admin_view_contact(request):
    contact = Contact.objects.all()
    return render(request, "admin_view_contact.html", {"contact":contact})


def admin_view_customer(request):
    customer = Customer.objects.all()
    return render(request, "admin_view_customer.html", {"customer":customer})

def admin_view_doctors(request):
    doctors = Doctors.objects.all()
    return render(request, "admin_view_doctors.html", {"doctors":doctors})

def admin_logout(request):
    request.session.flush()
    return redirect('/admin_login')


def accept_customer(request, id):
    customer = Customer.objects.get(id=id)
    customer.status = 'Accepted'
    customer.save()
    return redirect('/admin_view_customer')


def reject_customer(request, id):
    customer = Customer.objects.get(id=id)
    customer.status = 'Rejected'
    customer.save()
    return redirect('/admin_view_customer')


def accept_doctors(request, id):
    doctors = Doctors.objects.get(id=id)
    doctors.status = 'Accepted'
    doctors.save()
    return redirect('/admin_view_doctors')


def reject_doctors(request, id):
    doctors = Doctors.objects.get(id=id)
    doctors.status = 'Rejected'
    doctors.save()
    return redirect('/admin_view_doctors')

def my_profile(request):
    email = request.session["email"]
    users = Customer.objects.get(email=email)
    return render(request, "my_profile.html",{"users":users})


def my_profile_edit(request):
    email = request.session["email"]
    users = Customer.objects.get(email=email)
    return render(request,"update_my_profile.html",{"users":users})


def update_my_profile(request):
    if request.method == "POST":
        id = request.POST['id']
        users = Customer.objects.get(id=id)
        form = CustomerForm(request.POST,request.FILES, instance=users)
        if form.is_valid():
            form.save()
            return redirect('/my_profile')  # Redirect to a view where you display updated contact details
        else:
            print(form.errors)  # Print errors for debugging
    # If not a POST request or form is not valid, render the update form again
    return render(request, "update_my_profile.html", {})

def doctors_home(request):
    return render(request, "doctors_home.html", {})


def doctors_register(request):
    if request.method == 'POST':
        form = DoctorsForm(request.POST,request.FILES)
        email = request.POST['email']
        if form.is_valid():
            email=form.cleaned_data["email"]
            if Doctors.objects.filter(email=email).exists():
                return render(request, 'doctors_registration.html', {"msg": "This Email is Already Exists"})
            else:
                form.is_valid()
                form.save()
                return render(request, 'doctors_login.html', {"msg": "Successfully Register"})
        else:
            return render(request, 'doctors_registration.html', {"msg": "Invalid Data"})
    else:
        form = DoctorsForm()
        return render(request, 'doctors_registration.html', {"form":form})


def doctors_login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        if Doctors.objects.filter(email=email).exists():
            user = Doctors.objects.get(email=email)
            if user is not None:
                pwd = user.password
                if password == pwd:
                    if user.status == "Accepted":
                        request.session["email"] = email
                        return render(request, 'doctors_home.html', {})
                    else:
                        return render(request, "doctors_login.html", {"msg": "Account Is On Hold"})
                else:
                    return render(request, "doctors_login.html", {"msg": "Wrong Passwords"})
            else:
                return render(request, "doctors_login.html", {"msg": ""})
        return render(request, "doctors_login.html", {"msg": "Email Not Registered"})
    return render(request, "doctors_login.html", {})

def doctors_profile(request):
    email = request.session['email']
    doctors = Doctors.objects.get(email=email)
    return render(request, "doctors_profile.html", {"doctors":doctors})



def doctors_profile_edit(request):
    email = request.session["email"]
    doctors = Doctors.objects.get(email=email)
    return render(request,"doctors_profile_edit.html",{"doctors":doctors})


def update_doctors_profile(request):
    if request.method == "POST":
        id = request.POST['id']
        doctors = Doctors.objects.get(id=id)
        form = DoctorsForm(request.POST,request.FILES, instance=doctors)
        if form.is_valid():
            form.save()
            return redirect('/doctors_profile')  # Redirect to a view where you display updated contact details
        else:
            print(form.errors)  # Print errors for debugging
    # If not a POST request or form is not valid, render the update form again
    return render(request, "doctors_profile_edit.html", {})

def view_doctors(request):
    doctors = Doctors.objects.filter(status='Accepted')
    return render(request, "view_doctors.html", {"doctors": doctors})


def add_appoitments(request,id):
    email = request.session['email']
    doctors = Doctors.objects.get(id=id)
    if request.method == "POST":
        form = AppoitmentsForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, "add_appoitments.html", {"msg": "Successfully Saved"})
        return render(request, "add_appoitments.html", {})
    return render(request, "add_appoitments.html", {"email":email,"doctors":doctors})

def my_appoitments(request):
    email = request.session['email']
    appoitments = Appoitments.objects.filter(customer_email=email)

    return render(request,'my_appoitments.html',{"appoitments":appoitments})

def doctors_view_appoitments(request):
    email = request.session['email']
    appoitments = Appoitments.objects.filter(doctor_email=email)

    return render(request,'doctors_view_appoitments.html',{"appoitments":appoitments})


def accept_appoitments(request, id):
    appoitments = Appoitments.objects.get(id=id)
    appoitments.status = 'Accepted'
    appoitments.save()
    return redirect('/doctors_view_appoitments')


def reject_appoitments(request, id):
    appoitments = Appoitments.objects.get(id=id)
    appoitments.status = 'Rejected'
    appoitments.save()
    return redirect('/doctors_view_appoitments')

def add_prescriptions(request,id):
    email = request.session['email']
    appoitments = Appoitments.objects.get(id=id)
    if request.method == "POST":
        form = PrescriptionsForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, "add_prescriptions.html", {"msg": "Successfully Saved"})
        return render(request, "add_prescriptions.html", {})
    return render(request, "add_prescriptions.html", {"email":email,"appoitments":appoitments})

def view_prescriptions(request,id):
    appoitments = Appoitments.objects.get(id=id)
    prescriptions = Prescriptions.objects.filter(appoitments_id=appoitments.id)

    return render(request,'view_prescriptions.html',{"prescriptions":prescriptions})

def doctor_logout(request):
    request.session.flush()
    return redirect('/doctors_login')


def deactivate(request, id):
    customer = Customer.objects.get(id=id)
    customer.Status = 'pending'
    customer.save()
    return redirect('/customer_profile')

def is_login(request):
    if request.session.__contains__('email'):
        return True
    else:
        return False


def change_password(request):
    email = request.session["email"]
    print("hi")
    if is_login(request):
        if request.method == 'POST':
            password = request.POST["password"]
            new_password = request.POST["new_password"]
            email = request.session["email"]
            try:
                user = Customer.objects.get(email=email, password=password)
                user.password = new_password
                user.save()
                return render(request, "customer_login.html", {"msg": "Successfully Password Updated"})
            except Exception as e:
                print(e, "error")
            return render(request, "change_password.html", {"email": email, "msg": "Invalid Credentials"})
    return render(request, "change_password.html", {"email": email})


def admin_change_password(request):
    email = request.session["email"]
    print("hi")
    if is_login(request):
        if request.method == 'POST':
            password = request.POST["password"]
            new_password = request.POST["new_password"]
            email = request.session["email"]
            try:
                user = Admin.objects.get(email=email, password=password)
                user.password = new_password
                user.save()
                return render(request, "admin_login.html", {"msg": "Successfully Password Updated"})
            except Exception as e:
                print(e, "error")
            return render(request, "admin_change_password.html", {"email": email, "msg": "Invalid Credentials"})
    return render(request, "admin_change_password.html", {"email": email})


def add_notifications(request):
    if request.method == "POST":
        form =Add_notificationsForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, "add_notifications.html", {"msg":"Successfully Added"})
        return render(request, "add_notifications.html", {})
    return render(request, "add_notifications.html", {})


def view_notification(request):
    notifications = Notifications.objects.all()
    return render(request, "view_notification.html", {"notifications":notifications})


def customers_view_notification(request):
    notifications = Notifications.objects.all()
    return render(request, "customers_view_notification.html", {"notifications":notifications})



def add_pet(request):
    email = request.session['email']
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, "add_pet.html", {"msg":"Successfully Added"})
        return render(request, "add_pet.html", {})
    return render(request, "add_pet.html", {"email":email})


def my_pets(request):
    email = request.session['email']
    pets = Pet.objects.filter(email=email)
    return render(request, "my_pets.html", {"pets":pets})



def pet_edit(request,id):
    pets = Pet.objects.get(id=id)
    return render(request, "pet_edit.html", {'pets':pets})


def pet_update(request):
    if request.method == 'POST':
        email = request.POST['email']
        dog = Pet.objects.get(email=email)
        form = PetForm(request.POST, request.FILES, instance=dog)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/my_pets')
        return render(request, "pet_edit.html", {})
    return render(request, "pet_edit.html", {})


def delete_view_pet(request, id):
    pets = Pet.objects.get(id=id)
    pets.delete()
    return redirect('/my_pets')


def view_all_pets(request):
    email = request.session['email']
    customer = Customer.objects.get(email=email)

    # Exclude the user's own pets and annotate the like count
    pets = Pet.objects.exclude(email=email).annotate(like_count=Count('pets_likes'))

    # Get the list of pet IDs that the customer has already shown interest in
    interested_pet_ids = Interest.objects.filter(customer_id=customer.id).values_list('pet_id', flat=True)

    # Get the list of pet IDs that the customer has already liked
    liked_pets = Pets_Likes.objects.filter(customer_email=email).values_list('pets_id', flat=True)

    return render(request, "view_all_pets.html", {
        "pets": pets,
        "interested_pet_ids": interested_pet_ids,
        "liked_pets": liked_pets,
    })


def doctor(request, id):
    return render(request, "doctor.html", {})


def delete_view_notification(request, id):
    notifications = Notifications.objects.get(id=id)
    notifications.delete()
    return redirect('/view_notification')







def delete_view_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('/view_doctor')


# views.py


def book_now(request, id):
    doc = Doctor.objects.get(id=id)
    email = request.session['email']
    cus = Customer.objects.get(Email=email)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('view_bookings')  # Redirect to a success page or another view
    else:
        form = BookingForm()
    pet = Pet.objects.all()
    return render(request, 'booking_form.html', {'form': form, 'pet': pet, "x": doc, "y": cus})


# views.py



def view_bookings(request):
    book = Booking.objects.all()
    return render(request, "view_bookings.html", {"book": book})


def view_prescription(request):
    prescription = Prescription.objects.all()
    return render(request, 'view_prescription.html', {'prescription': prescription})


def view_precautions(request):
    email = request.session['email']
    precautions = Precautions.objects.filter(email=email)
    return render(request, 'view_precautions.html', {'precautions':precautions})

def customers_view_precautions(request):
    precautions = Precautions.objects.all()
    return render(request, 'customers_view_precautions.html', {'precautions':precautions})

def add_precautions(request):
    email = request.session['email']
    if request.method == "POST":
        form = PrecautionsForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, "add_precautions.html", {"msg": "Successfully Saved"})
        return render(request, "add_precautions.html", {})
    return render(request, "add_precautions.html", {"email":email})

def quote_view(request):
    doctor = Quote.objects.all()
    return render(request, 'view_quote.html', {'doctor': doctor})


def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quote_view')
    else:
        form = QuoteForm()

    return render(request, 'add_quote.html', {'form': form})


def add_reviews(request,id):
    email = request.session['email']
    doctors = Doctors.objects.get(id=id)
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_reviews.html', {"msg":"Successfully Saved"})
    else:
        form = ReviewsForm()

    return render(request, 'add_reviews.html', {'form': form,"doctors":doctors,"email":email})


def view_reviews(request,id):
    doctors = Doctors.objects.get(id=id)
    reviews = Reviews.objects.filter(doctors_id=doctors.id)
    return render(request, 'view_reviews.html', {'reviews':reviews})

def doctors_view_reviews(request):
    email = request.session['email']
    doctors = Doctors.objects.get(email=email)
    reviews = Reviews.objects.filter(doctors_id=doctors.id)
    return render(request, 'doctors_view_reviews.html', {'reviews':reviews})

def doctors_change_password(request):
    email = request.session["email"]
    print("hi")
    if is_login(request):
        if request.method == 'POST':
            password = request.POST["password"]
            new_password = request.POST["new_password"]
            email = request.session["email"]
            try:
                user = Doctors.objects.get(email=email, password=password)
                user.password = new_password
                user.save()
                return render(request, "doctors_login.html", {"msg": "Successfully Password Updated"})
            except Exception as e:
                print(e, "error")
            return render(request, "doctors_change_password.html", {"email": email, "msg": "Invalid Credentials"})
    return render(request, "doctors_change_password.html", {"email": email})


def view_all_customers(request):
    email = request.session['email']
    customers = Customer.objects.exclude(email=email)

    # Fetch the friend requests where the logged-in user is either the sender or receiver
    sent_requests = Friends_Requests.objects.filter(from_email=email)
    received_requests = Friends_Requests.objects.filter(to_email=email)

    # Combine both sender and receiver requests
    requested_ids = list(sent_requests.values_list('to_email', flat=True)) + list(received_requests.values_list('from_email', flat=True))

    # Fetch accepted friend requests (either direction)
    accepted_requests = Friends_Requests.objects.filter(
        (Q(from_email=email) | Q(to_email=email)),
        status='Accepted'
    ).values_list('from_email', 'to_email')

    # Convert accepted requests into a list of emails for easier lookup
    friends_ids = [request[0] if request[1] == email else request[1] for request in accepted_requests]

    return render(request, 'view_all_customers.html', {
        "customers": customers,
        "requested_ids": requested_ids,
        "friends_ids": friends_ids
    })

def add_friends_requests(request, id):
    email = request.session['email']
    customer = Customer.objects.get(id=id)

    # Check if the request already exists
    if Friends_Requests.objects.filter(from_email=email, to_email=customer.email).exists():
        return JsonResponse({"msg": "Request Already Sent"}, status=400)

    if request.method == "POST":
        # Create the friend request
        Friends_Requests.objects.create(
            customers=customer,
            from_email=email,
            to_email=customer.email
        )
        return JsonResponse({"msg": "Friend Request Sent"}, status=200)

    return JsonResponse({"msg": "Invalid Request"}, status=400)



def view_friends_requests(request):
    email = request.session['email']
    requests = Friends_Requests.objects.filter(to_email=email)
    return render(request,'view_friends_requests.html',{"requests":requests})


def accept_friends_requests(request, id):
    requests = Friends_Requests.objects.get(id=id)
    requests.status = 'Accepted'
    requests.save()
    return redirect('/view_friends_requests')


def reject_friends_requests(request, id):
    requests = Friends_Requests.objects.get(id=id)
    requests.status = 'Rejected'
    requests.save()
    return redirect('/view_friends_requests')


def my_friends(request):
    email = request.session['email']

    # Fetching friends where the logged-in user is either the sender or receiver, and the request is accepted
    sent_friends = Friends_Requests.objects.filter(from_email=email, status='Accepted')
    received_friends = Friends_Requests.objects.filter(to_email=email, status='Accepted')

    return render(request, 'my_friends.html', {
        "sent_friends": sent_friends,
        "received_friends": received_friends
    })

def add_posts(request):
    email = request.session['email']
    if request.method == "POST":
        form = Add_PostsForms(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, "add_posts.html", {"msg": "Successfully Saved"})
        return render(request, "add_posts.html", {})
    return render(request, "add_posts.html", {"email":email})

def admin_view_posts(request):
    posts = Add_Posts.objects.all()
    return render(request,'admin_view_posts.html',{"posts":posts})

def accept_posts(request, id):
    posts = Add_Posts.objects.get(id=id)
    posts.status = 'Accepted'
    posts.save()
    return redirect('/admin_view_posts')


def reject_posts(request, id):
    posts = Add_Posts.objects.get(id=id)
    posts.status = 'Rejected'
    posts.save()
    return redirect('/admin_view_posts')

def my_posts(request):
    email = request.session['email']

    posts = Add_Posts.objects.filter(email=email)
    return render(request,'my_posts.html',{"posts":posts})

def view_posts(request):
    email = request.session['email']

    # Get the user's friends (accepted friend requests)
    friend_pairs = Friends_Requests.objects.filter(
        (Q(from_email=email) | Q(to_email=email)),
        status='Accepted'
    ).values_list('from_email', 'to_email')

    # Flatten the friend pairs into a single list of emails, excluding the user's own email
    friends = set(chain(*friend_pairs)) - {email}

    # Get posts visible to all or only to friends if they are in the friend list
    posts = Add_Posts.objects.filter(
        Q(only_for='All') |
        (Q(only_for='Only_Friends') & Q(email__in=friends)),
        status='Accepted'
    ).exclude(email=email).annotate(like_count=Count('likes'))  # Count likes for each post

    # Get the posts liked by the user
    liked_posts = Likes.objects.filter(customer_email=email).values_list('post_id', flat=True)

    return render(request, 'view_posts.html', {
        "posts": posts,
        "liked_posts": liked_posts,
    })


def posts_edit(request,id):
    posts = Add_Posts.objects.get(id=id)
    return render(request, "posts_edit.html", {'posts':posts})


def posts_update(request):
    if request.method == 'POST':
        id = request.POST['id']
        posts = Add_Posts.objects.get(id=id)
        form = Add_PostsForms(request.POST, request.FILES, instance=posts)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/my_posts')
        return render(request, "posts_edit.html", {})
    return render(request, "posts_edit.html", {})




def delete_posts(request, id):
    posts = Add_Posts.objects.get(id=id)
    posts.delete()

    return redirect('/my_posts')

def like_post(request, post_id):
    email = request.session['email']
    post = get_object_or_404(Add_Posts, id=post_id)

    # Check if the user has already liked the post
    if not Likes.objects.filter(post=post, customer_email=email).exists():
        # Add the like
        Likes.objects.create(post=post, customer_email=email, date_time=timezone.now())
        msg = "Liked successfully."
    else:
        msg = "You've already liked this post."

    return redirect('view_posts')


def view_posts_likes(request,id):
    posts = Add_Posts.objects.get(id=id)
    likes = Likes.objects.filter(post_id=posts.id)
    return render(request,'view_posts_likes.html',{"likes":likes})


def add_comments(request,id):
    email = request.session['email']
    posts = Add_Posts.objects.get(id=id)
    comments = Add_Comments.objects.filter(posts_id=posts.id)
    if request.method == "POST":
        form = Add_CommentsForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, "add_comments.html", {"msg": "Successfully Saved","comments":comments})
        return render(request, "add_comments.html", {"comments":comments})
    return render(request, "add_comments.html", {"email":email,"posts":posts,"comments":comments})

def view_posts_comments(request,id):
    posts = Add_Posts.objects.get(id=id)
    comments = Add_Comments.objects.filter(posts_id=posts.id)
    return render(request,'view_posts_comments.html',{"comments":comments})

def express_interest(request, pet_id):
    email = request.session['email']

    # Get the customer object based on the session email
    customer = Customer.objects.get(email=email)

    # Check if the user has already expressed interest in this pet
    if not Interest.objects.filter(customer=customer, pet_id=pet_id).exists():
        # Get the pet and save the interest
        pet = Pet.objects.get(id=pet_id)
        Interest.objects.create(
            customer=customer,
            pet=pet,
            interest_date=timezone.now()
        )

    return redirect('view_all_pets')


def toggle_sell_status(request, id):
    # Get the pet by ID
    pet = Pet.objects.get(id=id)

    # Toggle the sell_for field
    if pet.sell_for == 'Yes':
        pet.sell_for = 'No'
    else:
        pet.sell_for = 'Yes'

    pet.save()

    # Redirect to 'my_pets' after updating the status
    return redirect('my_pets')

def view_pets_requests(request,id):

    pets = Pet.objects.get(id=id)


    requests = Interest.objects.filter(pet_id=pets.id)
    return render(request,'view_pets_requests.html',{"requests":requests})

def like_pets(request, pets_id):
    email = request.session['email']
    pets = get_object_or_404(Pet, id=pets_id)

    # Check if the user has already liked the post
    if not Pets_Likes.objects.filter(pets=pets, customer_email=email).exists():
        # Add the like
        Pets_Likes.objects.create(pets=pets, customer_email=email, date_time=timezone.now())
        msg = "Liked successfully."
    else:
        msg = "You've already liked this post."

    return redirect('view_all_pets')


def view_pets_likes(request,id):
    pets = Pet.objects.get(id=id)
    likes = Pets_Likes.objects.filter(pets_id=pets.id)
    return render(request,'view_pets_likes.html',{"likes":likes})

def doctors_view_notifications(request):
    notifications = Notifications.objects.all()
    return render(request, "doctors_view_notifications.html", {"notifications": notifications})

