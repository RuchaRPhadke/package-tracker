Package Tracker — DevOps CI/CD Mini Project

Overview:
This project is a Package Delivery Tracking System built using Flask and enhanced with a complete CI/CD pipeline. It simulates parcel tracking and demonstrates modern DevOps practices including automation, testing, containerization, and deployment.

Features:

* Track package status using tracking ID
* Dynamic status generation (Order Placed → Shipped → Out for Delivery → Delivered)
* Automated testing using Pytest
* Code quality checks using Pylint
* CI/CD pipeline using GitHub Actions
* Docker-based containerization

---

Project Structure:

```
package-tracker/
│
├── app/
│   └── app.py              # Main Flask application
│
├── tests/
│   └── test_app.py         # Unit tests
│
├── .github/workflows/
│   └── ci.yml              # CI/CD pipeline configuration
│
├── Dockerfile              # Container configuration
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

Installation and Setup:

1. Clone the repository:

```
git clone <your-repo-link>
cd package-tracker
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python app/app.py
```

4. Access in browser:

```
http://localhost:5000/track?id=1234
```

---

Running Tests:

```
pytest
```

---

CI/CD Pipeline:
The project uses GitHub Actions for Continuous Integration:

* Runs automatically on every push
* Installs dependencies
* Executes tests
* Performs code quality checks

---

Docker (Containerization):

Build Image:

```
docker build -t package-tracker .
```

Run Container:

```
docker run -p 5001:5000 package-tracker
```

Access Application:

```
http://localhost:5001/track?id=1234
```

---

Deployment:
The application is deployed in a staging environment using Docker containers and can be accessed locally via browser.

---

Key DevOps Concepts Demonstrated:

* Version Control using Git
* Continuous Integration (CI)
* Automated Testing
* Code Quality Analysis
* Containerization using Docker
* Deployment (Staging Environment)

---

Sample Output:

```
{
  "status": "Shipped"
}
```

---

Team Members:
435 Anushka Kondkar
439 Siddhani Magar
445 Bhargavee Mujbaile
454 Rucha Phadke

---

Conclusion:
This project demonstrates how DevOps practices can be applied to automate and streamline the software development lifecycle, ensuring faster and more reliable delivery.
Project completed as part of DevOps mini project.
