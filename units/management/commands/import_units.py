import pandas as pd
from django.core.management.base import BaseCommand
from units.models import DepartmentalUnit

class Command(BaseCommand):
    help = 'Bulk imports Departmental Units from an Excel file'

    def handle(self, *args, **kwargs):
        file_path = 'departmental_units.xlsx'
        
        try:
            df = pd.read_excel(file_path)
            self.stdout.write(self.style.WARNING(f"Found {len(df)} rows. Starting import..."))
            
            count_created = 0
            count_updated = 0

            # Check if the column is named 'Name' or 'name'
            name_col = 'Name' if 'Name' in df.columns else 'name'
            # Check if 'Code' or 'code' exists, otherwise set to None
            code_col = 'Code' if 'Code' in df.columns else ('code' if 'code' in df.columns else None)

            for index, row in df.iterrows():
                # Get the name, stripping any accidental whitespace
                name = str(row[name_col]).strip()
                
                # If the Excel has a Code column, use it. If not, set to None.
                if code_col:
                    code = str(row[code_col]).strip() if pd.notna(row[code_col]) else None
                else:
                    code = None
                
                # Update or create the record
                obj, created = DepartmentalUnit.objects.update_or_create(
                    name=name,
                    defaults={'code': code, 'is_active': True}
                )
                
                if created:
                    count_created += 1
                else:
                    count_updated += 1

            self.stdout.write(self.style.SUCCESS(
                f"Import Complete! Created: {count_created}, Updated: {count_updated}"
            ))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Error: Could not find {file_path} in the root directory."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))