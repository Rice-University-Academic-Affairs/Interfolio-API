# Interfolio FAR Python API

This library provides an intuitive and fully-tested Python interface to [Interfolio's Faculty Activity Reporting API](https://www.faculty180.com/swagger/ui/index.html). 

## Getting Started

There is one class, ```InterfolioFAR```, that you instantiate with your unique database ID, public API key, and private API key -- all of which must be obtained from directly from Interfolio.

You can pass these three values directly into the ```InterfolioFAR``` constructor or set them via the following environment variables:

- FAR_DATABASE_ID
- FAR_PUBLIC_KEY
- FAR_PRIVATE_KEY

### Direct Instantiation
```python
from src.interfolio_far import InterfolioFAR

far_api = InterfolioFAR(
    database_id="your_database_id",
    public_key="your_public_key",
    private_key="your_private_key"
)
```

### Instantiation from Environment Variables
```python
from src.interfolio_far import InterfolioFAR

far_api = InterfolioFAR()
```

## Usage Examples

For details on the various query parameters, consult [Interfolio's API documentation](https://www.faculty180.com/swagger/ui/index.html)

Critically, all API endpoints accept a `data` parameter, which takes one of three values:

- 'count' (default) - returns a count of the results
- 'summary' - which returns simplified results
- 'detailed' - which returns complex and thorough results

```python
from src.interfolio_far import InterfolioFAR

far_api = InterfolioFAR()

# Units
far_api.get_units(data="summary")
far_api.get_unit(unit_id="fake_id", data="summary")

# Terms
far_api.get_terms(yearlist="2017,2018,2019", data="summary")

# Users
far_api.get_users(employmentstatus="Full Time", data="summary")
far_api.get_user(user_id="fake_id", data="summary")

# Permissions
far_api.get_permissions(data="count")
far_api.get_permission(user_id="fake_id", data="summary")

# Faculty Classifications
far_api.get_faculty_classification_data(data="count")
far_api.get_faculty_classifications(data="summary")
far_api.get_faculty_classification(faculty_classification_id="fake_id", data="summary")

# Sections
far_api.get_sections(data="count")
far_api.get_section(section_id="fake_id", data="summary")

# Activities
far_api.get_activities_ids_for_sections(data="detailed", verbose="1", sectionid="fake_id")
far_api.get_activities_ids_for_section(section_id="fake_id", data="detailed")
far_api.get_activities_details_for_section(section_id="fake_id")
far_api.get_activity_details(section_id="fake_id", activity_id="fake_id", data="detailed")
far_api.get_activity_attachments(section_id="fake_id", activity_id="fake_id", data="detailed")
```
