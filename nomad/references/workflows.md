# Nomad Procedural Workflows

This document provides detailed guidance for executing the Nomad Vacation Planner workflows.

## Phase 0: The Consultation (Weather & Timing)
Before any routing or activity planning, you must validate the "When" and "Where".
1.  **Search**: Use `google_web_search` for `[Destination] weather in [Month]`, `[Destination] festivals [Month]`, and `[Destination] public holidays [Month]`.
2.  **Visa Verification**:
    *   **Citizenship**: Ask for the traveler's citizenship. If skipped, assume **American**.
    *   **Official Search**: Use `google_web_search` to find the **official embassy or government travel portal** (e.g., `site:gov.cn` or `site:state.gov`).
    *   **Deep Fetch**: Use `web_fetch` on the official URL to confirm current requirements. **Prohibit third-party aggregators.**
3.  **Analyze**: 
    *   Compare weather data with the user's "Comfort Zone" in their profile.
    *   Check for "Golden Weeks" or massive local holidays that lead to overcrowding.
4.  **Advise**: Present findings on weather, timing, and specific visa requirements found on official sites. "October is excellent for Beijing, but I recommend arriving after Oct 7th to avoid the National Day crowds."

## Phase 1: The Layout (Surface Search)
Focus on broad strokes and inter-city logistics.
1.  **Inter-city Travel**: Identify the logical flow (e.g., Beijing -> Xi'an -> Shanghai). 
    *   **Propose Transport**: Suggest 1-2 transport types (e.g., High-speed rail vs. Internal flights).
    *   **Logistics**: For each option, provide the **Estimated Duration** (e.g., "4.5 hours") and **Rough Pricing** (e.g., "$80 - $120").
2.  **Accommodation Areas**: Do not pick specific hotels yet. Suggest neighborhoods (e.g., "Stay near the Bell Tower in Xi'an for history and street food").
3.  **Activity Curation (The DNA Blend)**:
    *   Start with the **Top 3 "Must-Sees"** for the destination (The DNA).
    *   Overlay **User Interests**. If the user likes "Nature" and is in China, suggest Zhangjiajie or Tiger Leaping Gorge.
    *   **Provide Options**: For each day, suggest 3-4 diverse activity options (e.g., one "Active", one "Cultural", one "Relaxed") so the user can choose their preference.
    *   Filter by **Travel Mode**. If "Family", replace a 10-mile hike with a scenic gondola ride.

## Phase 2: Verification (The Deep Dive)
This phase is triggered by the `nomad verify` command or when the user approves Phase 1.
1.  **Platform Check**: Consult `~/.gemini/nomad_profile.md` for "Preferred Platforms".
2.  **Live Flights**: Search for real flight numbers and current "Starting at" prices using `google_web_search` scoped to preferred platforms (e.g., `site:kayak.com [Route] [Date]`).
3.  **Specific Hotels**: Pick 2-3 specific hotels in the approved neighborhoods. Check availability and rates on preferred platforms (e.g., `site:booking.com [Hotel Name] [Date]`).
3.  **Review Synthesis**: 
    *   **Volume**: Scan 5-7 top/recent reviews across Google, TripAdvisor, Yelp, and Booking.com.
    *   **Balanced Synthesis**:
        *   **Top Praise**: Identify the single strongest recurring positive (e.g., "Exceptional service" or "Authentic flavor").
        *   **Critical Flags**: Identify the most significant recurring negative (e.g., "Overpriced for the portion size" or "Construction noise nearby").
        *   **Destination Truths/Pro-Tips**: Capture actionable "insider" tips from reviews (e.g., "The street food market is great, but don't go after 10 PM" or "Ask for a high-floor room at Hotel X to avoid street noise").
    *   **Summary**: Present these as bullet points for each major recommendation in the final itinerary.
4.  **Booking Logic**:
    *   Find the direct booking URLs.
    *   Check for "Required Pre-booking" (e.g., "The Louvre requires timed entry tickets; current availability is good for your dates").

## Phase 3: Auxiliary Commands

### `nomad packing`
- **Inputs**: Current weather forecast + Activity list + Group dynamic.
- **Logic**: If "Kids" + "Rain", include "Compact travel umbrella and waterproof shoes for children." If "Art Museums" + "Walking", include "Stylish but comfortable walking shoes."

### `nomad budget`
- **Logic**: Create a table with categories: `Transport`, `Lodging`, `Activities`, `Daily Food (est.)`. 
- **Total**: Provide a "Low Estimate" and "High Estimate" total.

### `nomad profile`
Use this workflow to manage the user profile at `~/.gemini/nomad_profile.md`.
1.  **Check/List**: If a profile exists, read it and display a summary of current settings to the user.
2.  **Edit/Create Selection**: 
    *   If no profile exists: Proceed to a full sequential setup.
    *   If a profile exists: Ask the user if they want to update specific sections (e.g., "Interests", "Budget", "Travel Modes") or perform a full reset.
3.  **Gather Data**: Use `ask_user` with targeted questions based on the user's selection:
    *   **Interests**: Rank culinary, history, nature, etc. (1-5).
    *   **Logistics & Platforms**: 
        *   Ask for preferred airlines and hotel groups.
        *   **Lodging Preferences**: Ask about preferred style (Boutique, Chains, Hostels, Rentals) and budget level for accommodations.
        *   **MANDATORY**: Ask for preferred booking platforms for both flights (e.g., Kayak, Google Flights, Skyscanner) and accommodations (e.g., Booking.com, Airbnb, Hotels.com). This is critical for Phase 2 deep searches.
    *   **Dining (Skippable)**:
        *   **Dietary Restrictions**: Ask if they have specific dietary needs (Shellfish-free, No Pork, Halal, Kosher, Vegetarian, Vegan, Gluten-free). Explicitly state they can skip if none.
        *   **Food Budget**: Ask about their preferred dining style/budget (e.g., "Street food/Budget," "Casual/Mid-range," "High-end/Fine dining").
    *   **Comfort**: Ask about weather preferences and travel pace.
4.  **Merge & Save**: Update only the requested sections (keeping others intact) and write the updated Markdown to `~/.gemini/nomad_profile.md`.
5.  **Confirmation**: Show the final updated summary and confirm it's saved.
