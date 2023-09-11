# Interfolio API
A lightweight Python library for Interfolio.

> Note: Interfolio API is still in beta. It currently only supports the GET methods in the Faculty Activity Reporting application. 

## Installation

```commandline
pip install interfolio_api
```
## Quick Start 

### Faculty Activity Reporting

The Faculty Activity Reporting API requires a public/private key pair and a database ID. These can either be passed in directly as strings or set as environment variables.
* INTERFOLIO_PUBLIC_KEY
* INTERFOLIO_PRIVATE_KEY
* FAR_DATABASE_ID

If not passed in directly, these values are assumed to come from the environment.

If these values are not passed directly or found in the environment, an error will be raised.

```python
from interfolio_api import InterfolioFAR

# Passed directly
far = InterfolioFAR(
    public_key="<your_public_key>",
    private_key="<your_private_key>",
    database_id="<your_database_ID>"
)

# From environment
far = InterfolioFAR()
```
## Documentation

### Faculty Activity Reporting
Details on the parameters for each API method can be found in [Interfolio's documentation.](https://www.faculty180.com/swagger/ui/index.html) Required parameters are passed as positional arguments; optional parameters are passed as keyword args (**kwargs). 

#### Units
```python
from interfolio_api import InterfolioFAR
far = InterfolioFAR()

# Retrieve a listing of academic units
far.get_units()

# Retrieve details on a specific unit
far.get_unit(unit_id="<id>")
```

#### Terms
```python
from interfolio_api import InterfolioFAR
far = InterfolioFAR()

# Retrieve the 'term' periods that a school has set up
far.get_terms()
```

#### Users
```python
from interfolio_api import InterfolioFAR
far = InterfolioFAR()

# Retrieve basic identifying information for a listing of users
far.get_users()

# Retrieve a full profile for the specified user
far.get_user(user_id="<id>")

# Retrieve activity and section data for a listing of users
far.get_user_data()

# Retrieve a list of Tenant ID's for the current user
far.get_tenant_ids()
```

#### Permissions
```python
from interfolio_api import InterfolioFAR
far = InterfolioFAR()

# Retrieve permission information for a listing of users
far.get_permissions()

# Retrieve permission information for a specified user
far.get_permission(user_id="<id>")
```

#### Faculty Classifications
```python
from interfolio_api import InterfolioFAR
far = InterfolioFAR()

# Retrieve details on the available faculty classifications
far.get_faculty_classifications()

# Retrieve details on a specific faculty classification
far.get_faculty_classification(faculty_classification_id="<id>")

# Retrieve faculty classification data for a listing of users
far.get_faculty_classification_data()
```

#### Sections
```python
from interfolio_api import InterfolioFAR
far = InterfolioFAR()

# Retrieve details on sections
far.get_sections()

# Retrieve details for a specific section
far.get_section(section_id="<id>")
```

#### Activities
```python
from interfolio_api import InterfolioFAR
far = InterfolioFAR()

# Retrieve faculty activity IDs in sections
far.get_activities_ids_in_sections()

# Retrieve faculty activity IDs for a specific section
far.get_activities_ids_for_section(section_id="<id>")

# Retrieve faculty activity details for a specific section
far.get_activities_details_for_section(section_id="<id>")

# Retrieve details for a specific activity ID
far.get_activity_details(
    section_id="<id>",
    activity_id="<id>"
)

# Retrieve details for a given activity attachment
far.get_activity_attachments(
    section_id="<id>",
    activity_id="<id>"
)

# Retrieve activity classification data
far.get_activity_classifications()

# Retrieve details for a specific activity classification 
far.get_activity_classification(
    activity_classification_id="<id>"
)
```

#### Courses
```python
from interfolio_api import InterfolioFAR
far = InterfolioFAR()

# Retrieve course prefixes
far.get_course_prefixes()

# Retrieve details for multiple courses
far.get_courses()

# Retrieve details for courses taught during one or more terms
far.get_courses_taught()

# Retrieve details for a specific course taught during a specific term
far.get_course_taught(course_taught_id="<id>")

# Retrieve attachment details for a specific course taught during specific term
far.get_course_taught_attachments(
    course_taught_id="<id>"
)
```

#### Evaluations
```python
from interfolio_api import InterfolioFAR
far = InterfolioFAR()

# Retrieve evaluation details for multiple users
far.get_evaluations()
```

#### Vitae
```python
from interfolio_api import InterfolioFAR
far = InterfolioFAR()

# Retrieve details on all vitae
far.get_vitae()

# Retrieve details on a specific user's specific vita
far.get_vita(user_id="<id>", vita_id="<id>")

# Retrieve a list of vitae that the user is permissioned to select
far.get_paginated_vitae(tenant_id="<id>")
```

#### Attachments
```python
from interfolio_api import InterfolioFAR
far = InterfolioFAR()

# Download an attachment
far.download_attachment(attachment_id="<id>")
```