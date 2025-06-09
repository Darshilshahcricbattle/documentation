## Salary Cap Rules for Scoring Set Up
**Navigation**
**League Home > Rules > Scoring**

The **Scoring** section defines every way a user can earn or lose points based on the real cricket match, and contains settings for bonus/penalty rules, captains, impact players, milestone bonuses, and what to do in “No Result” matches.
All options and point values can be edited only by the League Manager. When any scoring rule is changed, past matches will also be rescored using the updated rules.

---

## 1. Modify Scoring Rules in Your League

* **Purpose:**
  Lets you set how points are awarded or deducted for all possible actions in fantasy cricket: batting, bowling, fielding, captains, and advanced conditions.
* **Warning:**
  If you change any rule after the league starts, the system will automatically rescore all previous matches to ensure fairness.

---

## 2. Predict the Winner of Ongoing Match

* **Allow predict the winner:**
  If enabled, users can make a prediction on which team will win each live/ongoing match.
* **Assign Bonus Points for correct prediction:**
  Points given if user’s prediction is correct.
  *Default:* +100 points
* **Assign Bonus Points for incorrect prediction:**
  Points deducted if the prediction is wrong.
  *Default:* -50 points

---

## 3. Emergency Conditions

* **Exclude No Result matches:**
  If enabled, matches declared as “No Result” (e.g., abandoned due to rain) do not count for any player’s fantasy points. If disabled, points from such matches are included.
* **Refund trades count for no result matches:**
  If enabled, any trades made for a No Result match are refunded (not counted against user’s trade quota). Only works if “Exclude No Result” is enabled.

---

## 4. Points and Rules Breakdown

Below are the detailed default scoring rules, broken by category. **Every value can be edited by the League Manager.**

---

### 4.1. MOM (Man of the Match)

* **Official Man of the Match:**
  +50 points (can be set between 0–100)

---

### 4.2. Common Rules

* **Bonus for starting in playing 11:**
  +5 points for every player in the actual playing XI
* **Bonus for each starting player in winning team:**
  +5 points for each player in winning team’s XI
* **Exclude all batting fantasy points for bowlers:**
  If enabled, bowlers do not earn fantasy points for their batting
* **Exclude all bowling fantasy points for batsmen & wicket-keepers:**
  If enabled, batsmen/wicketkeepers do not earn bowling points

---

### 4.3. Impact Player Fantasy Points

* **Count fantasy points for impact players:**
  If enabled, impact players can earn points for their performances
* **Bonus for playing as an impact player:**
  +5 points for being named as impact player
* **Bonus for impact player in the winning team:**
  +5 points if the impact player’s team wins

---

### 4.4. Batting Scoring

* **Run scored:**
  +1.0 point per run (editable, range: 1.0–4.0)
* **6 Run Bonus:**
  +2 points per six hit (range: 0–10)
* **4 Run Bonus:**
  +1 point per four hit (range: 0–8)

**Dismissal Penalties:**

* **Dismissed for duck:**
  -10 points for getting out on 0 (range: -50 to 0).
  *Exclude bowlers in dismissed for duck points:* If enabled, bowlers are exempt from this penalty.

* **Negative bonus for batsman getting out within 1 to X Runs:**
  -5 points if out within set runs (e.g., within 5 runs), can adjust the run threshold.
  *Exclude bowlers for negative bonus:* If enabled, bowlers are exempt.

---

**Run Rate Bonus:**

There are two models:

* **A. Run Rate Bonus by Formula:**
  *Formula:* A \* (Runs - (X/6)\*Balls)

  * Minimum balls to be faced for bonus (e.g., 6)
  * Choose “Okay” performance value (X runs in 6 balls, e.g., 7.50)
  * Multiplier A (e.g., 1.00)

  *Example:* 32 runs in 30 balls, A=1.5, X=5 → 1.5\*(32-(5/6)\*30)=10.5 pts

* **B. Run Rate Bonus by Range:**
  *Set minimum runs, minimum balls, and bonus/penalty for defined run rate ranges:*

  * 0.00–100.00: -30 points
  * 100.01–110.00: -10 points
  * 110.01–125.00: 0 points
  * 125.01–150.00: 10 points
  * 150.01–175.00: 15 points
  * 175.01–200.00: 20 points
  * 200.01 and above: 30 points
    You can configure both the run threshold and the bonus for each range.

---

**Milestone Bonus (Batting):**

* On reaching 25 runs: +10
* On reaching 40 runs: +15
* On reaching 60 runs: +20
* On reaching 80 runs: +25
* On reaching 100 runs: +40
* On reaching 150 runs: +80

*All values are editable (range: 0–100 for lower milestones, up to 200 for 150 runs).*

---

### 4.5. Bowling Scoring

* **Wicket:**
  +40 points per wicket (0–100)
* **Dot Balls:**
  +1 per dot ball (e.g., every 1 dot balls)
* **Wide Balls:**
  -1 per wide ball (-10 to 0)
* **No Balls:**
  -5 per no ball (-10 to 0)
* **Maiden over:**
  +40 per maiden over (0–100)
* **Bonus for wickets by LBW/Bowled:**
  +5 points per such wicket

---

**Economy Rate Bonus:**

* **A. By Formula:**
  *Formula:* A \* (Balls - (6/X)\*Runs)

  * Minimum balls to be bowled (e.g., 6)
  * "Okay" performance (e.g., 7.50 runs per 6 balls)
  * Multiplier A (e.g., 1.00)

  *Example:* 25 runs in 30 balls, A=1.5, X=7 → 1.5\*(30-(6/7)\*25)=12.86 pts

* **B. By Range:**
  Set minimum overs, runs per over ranges, and bonus/penalty:

  * 0.00–3.99 rpo: +30 points
  * 4.00–5.99: +20
  * 6.00–6.99: +10
  * 7.00–7.99: 0
  * 8.00–8.99: -5
  * 9.00–9.99: -10
  * 10.00+: -20

---

**Milestone Bonus (Bowling):**

* 2 wickets: +10
* 3 wickets: +20
* 4 wickets: +30
* 5 wickets: +40
* 6+ wickets: +60

---

### 4.6. Fielding Scoring

* **Catch:**
  +10 per catch
* **Stumping:**
  +20 per stumping
* **Direct Run out:**
  +10
* **Indirect Run out:**
  +10

**Bonus for fielders taking X number of catches:**

* **Minimum number of catches for bonus:**
  2 (editable)
* **Points for taking minimum catches:**
  +10

---

### 4.7. Power Players (Captain & Vice Captain)

* **Default Option:**

  * Captain: 2x points
  * Vice Captain: 1.5x points

* **Advance Option 1: Captain & 2nd Inning Captain**

  * Captain: 2x points
  * 2nd Inning Captain: 2x points for 2nd inning performance (must be submitted within 1 hour after match start)

* **Advance Option 2: Batting Captain & Bowling Captain**

  * Batting Captain: 2x points
  * Bowling Captain: 1.5x points

---

**Special Notes:**

* Substitute: If a substitute takes a catch or effects a run out, those points are NOT counted.
* Super Over: Only points from regulation time count; Super Over points do not count.

---

## Manager Notes and Best Practices

* **Only the League Manager can edit scoring rules; all changes are visible to participants for transparency.**
* **Scoring changes are retroactive for all completed matches.**
* **Configure advanced settings like impact players, milestones, economy formulas, and run rate/overs for a more customized fantasy experience.**
* **“No Result” logic is crucial for weather-affected games and protects users from unfair losses.**
* **Advanced captain options add more tactical depth for experienced players.**

---

**End of Scoring Section**
If you’d like the same level of detail for Extra Scoring, Leaderboards, or any other tab, just send the navigation path and screenshot.
