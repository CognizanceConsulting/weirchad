# CLAUDE.md

Training operations memory for Chad Weir. A future session reads this first and picks up where the last one left off. Source of truth is Chad's own TRAINING CONTEXT FILE V.2, dated 18 July 2026. This file mirrors it and adds session history.

Last updated: 25 November 2026.

Writing rules for every output in this project. No em dashes ever. No Oxford commas. Short sentences. Real numbers over vague language. One clear next step at the close. Sign off with name only.

---

## Current focus, ongoing block

Four priorities, in order:

1. Cardio and respiratory fitness.
2. Weight loss.
3. Core strength.
4. Shoulder and neck mobility to reduce tension headaches.

No event date. Consistency beats peaking. Review every 4 weeks.

---

## Weekly template

Six days on, one full rest day. Anchor session at 6:00am. Nightly wind-down at 9:30pm.

- Monday. Z2 endurance ride, 60 min. Nasal breathing throughout.
- Tuesday. Strength 40 min. Lower body 20, core 10, shoulder mobility 10.
- Wednesday. Intervals 45 to 60 min. Alternate weekly between threshold and VO2 max. Threshold is 3 x 10 min at Zone 4, 5 min easy. VO2 is 5 x 3 min near max, 3 min easy.
- Thursday. Modo Flow at the East Vancouver studio, 6:00am. Or Peloton Pilates 30 min if not attending.
- Friday. Strength 40 min plus 10 min core. Upper back and scapular emphasis.
- Saturday. Long ride 2 to 3 hr. Road, gravel or MTB.
- Sunday. Rest, or an easy 45 min spin plus mobility.

Nightly, every day. 20 to 45 min Yin, Restorative or Slow Flow. Non negotiable. This is the headache lever.

---

## How each priority is trained

**Cardio and respiratory.** Roughly 80 percent of ride time in Zone 2, 20 percent hard. Breathing work 10 min on Monday and Thursday. Nasal only on all Zone 2 rides. Retest FTP every 6 to 8 weeks.

**Weight loss.** Deficit 400 to 500 kcal per day. Protein 1.8 to 2.2 g per kg across 4 feeds. Red meat 1 to 2 meals per week. Processed food, sugary drinks and refined baked goods out. Carbs timed around Wednesday and Saturday sessions. Half the plate vegetables. Alcohol near zero. Weigh in weekly, same day, same time. Track the 4 week trend. Sleep 7 to 8 hr.

**Core.** Two 10 min core blocks per week inside Tuesday and Friday strength. One Pilates session per week, 30 min. Anti-rotation and anti-extension focus. Pallof press, dead bug, bird dog, side plank, hollow holds. Skip high rep flexion, which aggravates neck tension.

**Shoulder, neck and tension headaches.** This priority needs daily contact. Daily 10 to 15 min at 9:30pm. Foam roller thoracic extensions, open books, wall slides, band pull aparts, face pulls, pec doorway stretch, upper trap and levator scapulae stretch, thread the needle. Strengthen stabilisers with face pulls, prone Y and T raises, deep neck flexor work. Audit desk and bike fit. On the bike keep soft elbows, shoulders down, change hand position often. Track hydration and caffeine against a simple headache log. If headaches are frequent, persistent or changing, get a physiotherapy assessment. Do not assume posture is the only cause.

---

## Systems and access

**Google Calendar.** Master time block. Target calendar is named Exercise/Workout. Resolve the ID by name with list_calendars. Do not hardcode it in this public-readable file. All events Busy, Colour ID 10, exact class named in the description. Outdoor sessions and studio classes are Google Calendar only. They are not Peloton classes.

**Peloton.** No API and no connector. Never request or accept login credentials. All Peloton actions run through Claude in Chrome in Chad's own logged in session. Scheduling is limited to the next 2 weeks, so it is a rolling job every fortnight. Peloton will not schedule the same class twice, so vary the instructor on repeats. Lower Body Strength is titled Glutes and Legs Strength in app. Peloton Schedule holds only Peloton classes.

**Modo Yoga, East Vancouver.** Booking runs through Mariana Tek, readable only via Claude in Chrome. Thursday target is 6:00am Modo Flow. No latecomers. Never book or pay automatically. Chad stays on Yoga 10 class cards at one studio class per week. Reconsider a membership only at 2 classes per week sustained.

**This Claude Code environment.** Google Calendar access yes. Claude in Chrome no. So Peloton scheduling and Modo booking cannot run from a Claude Code session. They stay in Chad's browser.

---

## Operating rules

1. Show the plan before writing to the calendar. Chad reviews first, then says go.
2. Never make a purchase, booking or payment on his behalf.
3. Never request or store login credentials. Browser agent inside his own session only.
4. Outdoor sessions and studio classes are Google Calendar only.
5. Google Calendar is the master time block. Peloton Schedule holds only Peloton classes.
6. Writing rules above apply to every output.

---

## History

**V.1, 8 June to 8 July 2026.** A 4 week build into a 3 day Chilcotin backcountry MTB tour. 6 training days per week, 1 rest. 6:00am anchor. Two Z2 rides, one interval ride, two strength sessions, one hot yoga class, one long weekend ride, one back to back ride per week. Progressive weeks 1 to 3, then a 30 percent cut and a 2 day taper. Tour complete.

**V.2 reset, 18 July 2026.** Tour block closed. Focus reset to the four priorities above. Ongoing block, no event date.

**Claude Code session, this thread.** Early drafts of a generic 30 day plan were made before V.2 was supplied. They are superseded. See note on the stale file below. After V.2, confirmed owner access on the Exercise/Workout calendar. Found two things already on it. First, recurring placeholders titled Wake Up & Work Out at 4:00am. These conflict with the 6:00am anchor in the template and the conflict is unresolved. Second, Monday chiropractic visits at Foundation Body Lab with Dr Oliver Sanchez, which fits the neck and shoulder priority. Proposed a Week 1 calendar load for review. Awaiting Chad's go, and his call on 6:00am versus the existing 4:00am slot.

---

## Stale file

`30-day-workout-plan.md` in this repo is an early generic draft from before V.2. It is not the real plan. Remove it or ignore it. The system in this file supersedes it.

---

## Open items

1. Current weight and target weight. Needed to set exact calorie and protein numbers.
2. Headache baseline. Frequency per week, typical severity, known triggers.
3. Injury and niggle list.
4. Book the 20 min bike fit check on bar height and reach. Carried from V.1.
5. Desk and monitor ergonomics audit.
6. Resolve 6:00am versus 4:00am anchor, then load the weekly template into the Exercise/Workout calendar.
7. Run the rolling Peloton scheduling for the first 2 weeks. Browser session only.
8. Confirm whether Nicole's Modo guest passes renew each cycle.
9. Schedule an FTP retest to set current zones.
