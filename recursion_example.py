#!/usr/bin/env python3
company = {
    "sales": [
        {
            "name": "Alice",
            "salary": 10000
        },
        {
            "name": "Bob",
            "salary": 8950
        }
    ],
    "development": {
        "frontend": [
            {
                "name": "Peter",
                "salary": 6500
            },
            {
                "name": "Alex",
                "salary": 8300
            }
        ],
        "backend": [{
            "name": "Pavel",
            "salary": 7100
        }]
    }
}


def sum_salaries(department):
    # base case
    if isinstance(department, list):
        return sum(person["salary"] for person in department)
    return sum(sum_salaries(dep) for dep in department.values())


sum_salaries(company)
