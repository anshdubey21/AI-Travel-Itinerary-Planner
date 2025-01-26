import streamlit as st 

def get_initial_details():
    destination = st.text_input("Where do you want to go?")
    budget = st.selectbox("What's your budget?", ["Low", "Moderate", "Luxury"])
    duration = st.number_input("How many days will your trip last?", min_value=1, step=1)
    purpose = st.selectbox("What’s the purpose of your trip?", ["Leisure", "Adventure", "Cultural", "Business"])
    preferences = st.text_area("Any special preferences (e.g., food, activities, mobility needs)?")
    
    if st.button("Next"): 
        return destination, budget, duration, purpose, preferences
    return None, None, None, None, None

def refine_preferences():
    spots = st.selectbox("Do you prefer exploring popular spots or hidden gems?", ["Popular Spots", "Hidden Gems", "Both"])
    pace = st.selectbox("Do you prefer a relaxed or action-packed itinerary?", ["Relaxed", "Action-packed"])
    food_pref = st.text_input("Any dietary restrictions or food preferences?")
    accommodation = st.selectbox("What type of accommodation do you prefer?", ["Budget", "Mid-range", "Luxury"])
    
    if st.button("Generate Itinerary"):
        return spots, pace, food_pref, accommodation
    return None, None, None, None

def generate_itinerary(destination, duration, budget, purpose, preferences, spots, pace, food_pref, accommodation):
    itinerary = f"""
    **Your {duration}-day Itinerary to {destination}:**
    
    - Budget: {budget}
    - Purpose: {purpose}
    - Preferences: {preferences}
    - Accommodation: {accommodation}
    
    **Day 1:**
    - Morning: Explore top attractions
    - Afternoon: Try local cuisine at a popular spot
    - Evening: Relax with a scenic view
    
    **Day 2:**
    - Morning: Cultural tour
    - Afternoon: Adventure activity
    - Evening: Fine dining experience
    
    Enjoy your trip!
    """
    st.markdown(itinerary)

if __name__ == "__main__":
    st.title("AI Travel Itinerary Planner")
    destination, budget, duration, purpose, preferences = get_initial_details()

    if destination:
        spots, pace, food_pref, accommodation = refine_preferences()
        if spots:
            generate_itinerary(destination, duration, budget, purpose, preferences, spots, pace, food_pref, accommodation)
