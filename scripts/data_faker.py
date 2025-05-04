"""
Data Faker module

This module provides functions to generate fake data using the Faker library.
"""

import pandas as pd
from faker import Faker
import random

def generate_fake_data(num_entries: int = 5, fields: list = None) -> pd.DataFrame:
    """
    Generate fake data with specified number of entries and fields.
    
    Args:
        num_entries (int): Number of data entries to generate (default: 5)
        fields (list): List of fields to include in the generated data. If None, 
                      uses default fields: ['Name', 'Address', 'Email', 'Phone Number',
                      'Date of Birth', 'Random Number', 'Job Title', 'Company', 'Lorem Ipsum Text']
        
    Returns:
        pd.DataFrame: DataFrame containing the generated fake data
    """
    fake = Faker()
    
    if fields is None:
        fields = [
            'Name', 'Address', 'Email', 'Phone Number',
            'Date of Birth', 'Random Number', 'Job Title',
            'Company', 'Lorem Ipsum Text'
        ]
    
    data = []

    try:
        for _ in range(num_entries):
            entry = {}
            for field in fields:
                if field == 'Name':
                    entry[field] = fake.name()
                elif field == 'Address':
                    entry[field] = fake.address()
                elif field == 'Email':
                    entry[field] = fake.email()
                elif field == 'Phone Number':
                    entry[field] = fake.phone_number()
                elif field == 'Date of Birth':
                    entry[field] = fake.date_of_birth(minimum_age=18, maximum_age=65).strftime("%Y-%m-%d")
                elif field == 'Random Number':
                    entry[field] = random.randint(1, 100)
                elif field == 'Job Title':
                    entry[field] = fake.job()
                elif field == 'Company':
                    entry[field] = fake.company()
                elif field == 'Lorem Ipsum Text':
                    entry[field] = fake.text()
            data.append(entry)

        return pd.DataFrame(data)

    except Exception as e:
        raise Exception(f"Error generating fake data: {str(e)}")    
    
    
