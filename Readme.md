# CodeBuddy

CodeBuddy is a web application designed to facilitate collaborative coding. It's aimed at students and professionals who want to code together, share knowledge, and collaborate on projects. The application is built using Django and includes features like coding rooms, user profiles, and chat.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)

## Features

- **Coding Rooms**: Create and join coding rooms to collaborate with others.
- **User Profiles**: Manage your profile and see profiles of other users.
- **Real-time Chat**: Communicate with your team in real time.
- **Search Bar**: Find coding rooms and users easily.
- **Authentication**: User login and registration.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Deployment**: Zappa, S3 bucket

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/princesharma74/CodeBuddy-Django-Project.git
   cd CodeBuddy-Django-Project
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Usage

1. **Sign up**: Create an account.
2. **Login**: Access your account.
3. **Create a coding room**: Start a new coding session.
4. **Join a coding room**: Collaborate with others in existing rooms.
5. **Chat**: Use the chat feature to communicate with your team.

## Deployment

CodeBuddy is deployed using Zappa and an S3 bucket. To deploy your own instance:

1. **Install Zappa**:
   ```bash
   pip install zappa
   ```

2. **Initialize Zappa**:
   ```bash
   zappa init
   ```

3. **Deploy**:
   ```bash
   zappa deploy production
   ```

For more details, refer to the [Zappa documentation](https://github.com/zappa/Zappa).

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

1. **Fork the repository**
2. **Create a new branch**:
   ```bash
   git checkout -b feature-branch
   ```

3. **Commit your changes**:
   ```bash
   git commit -m 'Add some feature'
   ```

4. **Push to the branch**:
   ```bash
   git push origin feature-branch
   ```

5. **Create a pull request**

## Contact

If you have any questions, feel free to open an issue or contact me at [princesharma2899@gmail.com].

---

*Deployed version: [Click here](https://yw0d0v4kp0.execute-api.ap-south-1.amazonaws.com/dev/) To use the API of this project. Use [this](https://1d29p3txbb.execute-api.ap-south-1.amazonaws.com/dev) link.*