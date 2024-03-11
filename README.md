# Sbitar - Hospital Management System

Welcome to Sbitar - a comprehensive Hospital Management System designed to streamline operations and enhance efficiency in healthcare facilities. This open-source web application is built using Django on the backend and HTML/CSS on the frontend, offering a user-friendly interface coupled with powerful functionality.

## Features
- **Patient Management:** Keep track of patient records, including personal information, medical history, and treatment plans.
- **Doctor Management:** Manage doctor profiles, including specialization, contact information, and availability.
- **Appointment Scheduling:** Efficiently manage appointments for patients with available doctors.
- **Room Allocation:** Allocate rooms for patients based on their requirements and availability.
- **Appointment Results:** Record and manage the results of appointments, including diagnoses, prescriptions, and follow-up plans.
- **Simple Dashboard:** Access a simple dashboard for an overview of key metrics and activities.
- **User Authentication and Authorization:** Secure login system to control access levels for different users.
- **Responsive Design:** Ensures compatibility across various devices and screen sizes.

## Installation
Follow these steps to set up Sbitar on your local machine:

1. Clone the repository:

    ```bash
    git clone https://github.com/chetanis/Sbitar.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Sbitar
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application at http://localhost:8000 in your web browser.

## Usage
- **Admin Panel:** Access the admin panel at http://localhost:8000/admin to manage patient records, appointments, doctors, rooms, and more.
- **Adding Patients:** Use the interface to add new patients to the system, including relevant details such as medical history and contact information.
- **Doctor Management:** Manage doctor profiles, including specialization, and availability.
- **Scheduling Appointments:** Schedule appointments for patients with available doctors, with options for date and time.
- **Managing Rooms:** Allocate rooms for patients based on their requirements and availability.
- **Recording Results:** Record and manage the results of appointments, including diagnoses, prescriptions, and follow-up plans.
- **Patient's History:** Access the history of a patient's appointments, including previous diagnoses, prescriptions, and treatments.
- **Viewing Dashboard:** Access a simple dashboard for an overview of key metrics and activities.


## Contributing
We welcome contributions from the community to enhance the functionality and usability of Sbitar. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.


## Contact
For any inquiries or support regarding Sbitar, please contact [anis73chetouane@gmail.com].
