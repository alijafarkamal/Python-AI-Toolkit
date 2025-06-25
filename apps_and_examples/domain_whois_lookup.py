import whois

def get_domain_info(domain_name):
    try:
        # Query the domain information
        domain = whois.whois(domain_name)
        print(f"Domain Name: {domain.domain_name}")
        print(f"Registrar: {domain.registrar}")
        print(f"Creation Date: {domain.creation_date}")
        print(f"Expiration Date: {domain.expiration_date}")
        print(f"Name Servers: {', '.join(domain.name_servers)}")
    except Exception as e:
        print(f"Error fetching information: {e}")

# Example usage
if __name__ == "__main__":
    domain = input("Enter a domain name (e.g., example.com): ")
    get_domain_info(domain)
