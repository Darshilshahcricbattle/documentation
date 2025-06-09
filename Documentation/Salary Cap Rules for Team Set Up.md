## Salary Cap Rules for Team Set Up
 **Nagivation** 
 **League Home > Rules > Team**

The **Playing Team** and associated configuration options let the League Manager control the fundamental composition, flexibility, and competitive structure of fantasy teams in the league. This section is crucial for shaping user experience and balancing fairness, skill, and variety.

---

### Playing Team Options

#### Number of teams per league
- **Description:** Sets the total number of teams that can participate in the league. All spots must be filled before the league begins.
- **Default:** Unlimited
- **Current Value (Example):** 15
- **Editable:** Yes, by League Manager.

#### Team Composition (Custom Combinations)
- The following variables can be adjusted if the League Manager purchases the "team combination" feature (premium).
  - **Total Players per team:** How many players each participant can select.  
    *Default: 11*  
  - **Total Players playing in Fantasy team:** Number of players from the squad that are active in the fantasy lineup.  
    *Default: 11*
  - **Total Players on Bench:** Number of bench players allowed (unused by default, can be set for advanced leagues).  
    *Default: 0*
  - **Minimum/Maximum by role:** Minimum/maximum counts for batsmen, bowlers, all-rounders, wicketkeepers, etc.  
    *Example:* Min 3/3/1/1, Max 6/6/4/4

#### Maximum budget allowed to select players
- **Description:** Caps the total budget each user has for selecting their squad, introducing a salary cap mechanic for strategy.
- **Default:** 100
- **Editable:** Yes

#### Maximum number of overseas players allowed
- **Description:** Restricts the maximum number of non-domestic (overseas) players per fantasy team, mirroring real-world league rules.
- **Default:** 4
- **Editable:** Yes

#### Minimum number of uncapped players to be selected
- **Description:** Optionally enforces selection of a minimum number of uncapped (non-international) players, useful for advanced or realistic leagues.
- **Default:** NA (Not enforced)
- **Editable:** Yes, with premium

#### Variable salary of players
- **Description:** If enabled, a player’s salary will increase or decrease automatically based on their real-life performance throughout the tournament. This can affect overall team budgets dynamically.
- **Default:** No
- **Purchased:** Premium option (Rs 2000)

#### Auto swap bench players
- **Description:** Controls whether and how players from the bench are automatically substituted into the active lineup.
  - **Do not allow auto swap:** Bench swaps must be done manually; no automation.
  - **Auto swap by priority:** Highest-priority bench players are automatically substituted if needed.
  - **Auto swap by points:** Bench players with the most points are auto-substituted.
- **Editable:** Yes

---

### Advanced Team Structure

These premium features add flexibility or advanced scenarios for league setup.

#### Pick real teams in fantasy team
- **Description:** Lets users select entire real-world teams (e.g., "India", "Australia") for their fantasy squad. Useful for certain contest types or experimental formats.
- **Default:** No  
- **Premium:** Rs 4000

#### Pick dummy players in fantasy team
- **Description:** Allows addition of "dummy" players to fill roster spots when real players are insufficient. Dummy players score zero points and maintain team structure for leagues with custom team sizes.
- **Default:** No  
- **Premium:** Rs 4000

#### Number of Player Sets
- **Description:** Allows for player duplication, useful in smaller leagues or experimental formats (e.g., if set to 2, each real player appears twice in the draft pool).
- **Default:** 1  
- **Editable:** Yes

---

### Player Customization

Allows detailed control over player attributes, for advanced leagues.

#### Change player role/category/base bid value
- **Description:** League Manager can modify the role (e.g., batsman, bowler), player category, or base auction price for any player in the pool.
- **Premium:** Rs 1000

#### Change salary of the players
- **Description:** Allows direct editing of individual player salaries, overriding system defaults.
- **Premium:** Rs 1000

---

### Team Lock Rules

These options control when and how teams can be edited before and during matches.

#### Player Lock Time (minutes before match)
- **Description:** Sets a deadline (in minutes) before the scheduled match start, after which team changes are locked.
- **Default:** 30 minutes
- **Premium:** Rs 3000

#### Make opponent’s team invisible
- **Description:** Controls when your team and other managers’ teams become visible to the rest of the league.
  - **No:** Teams always visible
  - **Before match starts:** Teams remain hidden until the next match or round starts
  - **Till match ends:** Teams remain hidden until the end of the match or round
- **Premium:** Rs 1500

#### Lock team changes (sub-options)
- **Do not lock team changes:** Teams remain editable at all times.
- **Lock Team Changes:** Several granular lock types:
  - **Lock Trades:** No new players can be brought in.
  - **Lock Team to Bench:** Cannot move players between active and bench slots.
  - **Lock C/VC:** Cannot change Captain or Vice-Captain.
  - **Apply to:** Either from first match start or from the current time.
- **Premium:** Rs 1000

#### Schedule Unlock Timings
- **Description:** Lets League Manager schedule temporary unlock periods for team changes. Once the scheduled period expires, original lock settings are restored. This aids in accommodating special scenarios or fixing issues without fully unlocking the league.

---

### Team Submission Rules

#### Enable Team submission in advance
- **Description:** Lets users create and submit teams for multiple upcoming matches (helpful for users in different time zones or with limited availability).
- **Default:** No  
- **Premium:** Rs 3000

#### Choose format for team updation
- **Description:** Controls whether teams are updated on a per-match, per-day, or per-round basis, allowing more flexibility in league operations.
- **Default:** Match  
- **Premium:** Rs 1000

#### Lock the round/day after the first match starts (Team submit deadline)
- **Description:** If enabled, teams are locked for an entire round or day as soon as the first match in that segment begins. Useful for formats with multiple matches per day or round.
- **Default:** No  
- **Premium:** Rs 1000

---

### Editing and Permissions

- **Who can edit:** Only the League Manager (creator) can change these settings.
- **Premium settings:** Marked above with their associated one-time costs (in INR).
- **Update required:** Click the **Update** button at the bottom after making any changes to save settings.

---

### Practical Guidance

- These settings control team diversity, strategy, and league fairness.
- Strict budgets and overseas player limits prevent "stacking" of superteams.
- Auto swaps and advanced structures allow for more casual or more hardcore fantasy gameplay.
- Team lock and submission rules let you tailor the league for both highly competitive and friendly play.

---

Continue to the next section (e.g., **Rules > Boosters**, **Rules > Scoring**, etc.) for further configuration options.
