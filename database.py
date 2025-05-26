from auth import supabase

def insert_user_profile(user_id, full_name):
    """Insert a new user profile into the database."""
    return supabase.table('profiles').insert({
        'id': user_id,
        'full_name': full_name
    }).execute()
 