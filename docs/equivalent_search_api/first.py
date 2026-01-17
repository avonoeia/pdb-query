import requests
import json

def search_pdb_china_funding():
    """
    Searches the RCSB PDB for SARS-CoV-2 structures solved by X-ray diffraction
    where the funding organization includes 'China'.
    """
    search_url = "https://search.rcsb.org/rcsbsearch/v2/query"

    # Define the search query using the RCSB PDB JSON schema
    # Logic: (Organism == SARS-CoV-2) AND (Method == X-RAY) AND (Funding contains "China")
    query = {
        "query": {
            "type": "group",
            "logical_operator": "and",
            "nodes": [
                {
                    "type": "terminal",
                    "service": "text",
                    "parameters": {
                        "attribute": "rcsb_entity_source_organism.taxonomy_lineage.name",
                        "operator": "contains_phrase",
                        "value": "SARS-CoV-2"
                    }
                },
                {
                    "type": "terminal",
                    "service": "text",
                    "parameters": {
                        "attribute": "exptl.method",
                        "operator": "exact_match",
                        "value": "X-RAY DIFFRACTION"
                    }
                },
                {
                    "type": "terminal",
                    "service": "text",
                    "parameters": {
                        "attribute": "pdbx_audit_support.funding_organization",
                        "operator": "contains_words",
                        "value": "China"
                    }
                }
            ]
        },
        "request_options": {
            "return_all_hits": True
        },
        "return_type": "entry"
    }

    try:
        # 1. Send the Search Request
        response = requests.post(search_url, json=query)
        response.raise_for_status()
        
        results = response.json()
        pdb_ids = results.get('result_set', [])
        
        count = len(pdb_ids)
        print(f"Found {count} PDB entries matching criteria.\n")
        
        # 2. Fetch details for the first 5 entries to demonstrate data retrieval
        # (Fetching all would take a long time in a simple loop)
        if count > 0:
            print("Details for the first 5 entries:")
            print("-" * 60)
            
            for pdb_id in pdb_ids[:5]:
                get_entry_details(pdb_id["identifier"])
                
            print("-" * 60)
            # print(f"Full list of PDB IDs: {pdb_ids}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error during search request: {e}")

def get_entry_details(pdb_id):
    """
    Fetches summary data for a specific PDB ID using the RCSB Data API.
    """
    data_url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}"
    
    try:
        resp = requests.get(data_url)
        if resp.status_code == 200:
            data = resp.json()
            title = data.get('struct', {}).get('title', 'No Title')
            date = data.get('rcsb_accession_info', {}).get('initial_release_date', 'Unknown Date')
            
            print(f"ID: {pdb_id}")
            print(f"Date: {date}")
            print(f"Title: {title}\n")
        else:
            print(f"ID: {pdb_id} (Could not retrieve details)")
            
    except Exception as e:
        print(f"Error fetching data for {pdb_id}: {e}")

if __name__ == "__main__":
    search_pdb_china_funding()