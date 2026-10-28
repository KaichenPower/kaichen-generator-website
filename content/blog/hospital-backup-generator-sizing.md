---
title: "Diesel Generator for Hospital Backup Power: Sizing Guide"
date: "2026-10-28"
excerpt: "How to size a diesel generator for hospital backup power: load schedule, kVA calculation, motor starting, fuel autonomy, noise limits and load bank testing."
image: "/images/blog/hospital-generator-sizing.jpg"
---

![Silent diesel generator set built for hospital standby power in our Yangzhou factory](/images/blog/hospital-generator-sizing.jpg)

# Diesel Generator for Hospital Backup Power: Sizing Guide

A hospital blackout is not an inconvenience. Within seconds of the mains dropping, the operating theatre loses its lighting, the ventilators in ICU fall back on batteries that last minutes rather than hours, the blood bank refrigerators start to drift above 6 °C, the lifts stop between floors with patients inside, and the nurse call system goes dark.

That is why a **diesel generator for hospital backup power** is specified differently from a generator for a factory or a construction site. It is not simply "the biggest set that fits the budget". It is a life-safety machine whose capacity, starting behaviour, fuel autonomy, acoustic performance and test record all have to be defensible to an accreditation inspector.

This guide walks through the actual engineering sequence we use when sizing hospital sets: build the load schedule, convert to kVA with the right corrections, check motor starting, then settle fuel, redundancy, noise and testing. The reference figures come from our own KC series datasheets, including two real hospital-class units.

## 1. What a hospital generator actually has to carry

Hospital electrical systems are usually split into a normal supply and one or more essential buses. Only the essential buses land on the generator. Getting the boundary right is half the sizing job.

| Load group | Typical contents | What it means for sizing |
|---|---|---|
| Life safety | Operating theatre and ICU lighting, fire alarm, smoke extraction, emergency egress lighting, medical gas alarms | Must transfer within about 10 seconds; never allowed to be shed |
| Critical | ICU and NICU equipment, dialysis, blood bank refrigeration, pharmacy cold chain, laboratory incubators, IT and nurse call | Clean, stable voltage matters more than raw capacity |
| Equipment | Lifts, water pumps, fire pump, air handling, sterilisation, kitchen and laundry (partial) | Dominated by motor starting, not by running kW |
| Optional / non-essential | General ward sockets, standard air conditioning, some kitchen loads | Usually excluded, or shed automatically on generator overload |

Two practical rules follow from this table. First, do not put the whole hospital on the generator unless the budget and the fuel storage genuinely support it — most projects run 40–60 % of connected load on the essential bus. Second, treat motor loads as a starting problem, not a running problem; a 15 kW lift motor can demand five to seven times its rated current for a second or two.

The code framework differs by country — NFPA 99 and NFPA 110 in the United States, HTM 06-01 in the United Kingdom, IEC 60364-7-710 for medical locations in Europe and many export markets. They disagree on details but agree on the essentials: a defined essential bus, a defined transfer time, a defined fuel duration, and documented periodic testing. Confirm the local version before you fix the kVA.

## 2. Build the load schedule before you talk about kVA

Every hospital sizing argument we have ever had was really an argument about the load schedule. Do this first, in a spreadsheet, circuit by circuit.

For each item record four things: nameplate kW, power factor, demand factor (how much of it actually runs at once), and starting method (direct-on-line, star-delta, soft starter, VFD).

Here is a worked example for a 200-bed general hospital where chillers, kitchen and laundry are on the essential bus. These are illustrative planning figures, not a substitute for the project's own single-line diagram:

| Load | Connected kW | Demand factor | Running kW |
|---|---|---|---|
| Theatre, ICU, emergency lighting, fire systems | 120 | 1.0 | 120 |
| ICU/NICU equipment, blood bank, pharmacy, IT | 90 | 1.0 | 90 |
| Lifts (4 × 15 kW) | 60 | 0.6 | 36 |
| Chiller (one machine on essential bus) | 90 | 1.0 | 90 |
| Pumps, water treatment, fire pump (standby) | 55 | 1.0 | 55 |
| Kitchen and laundry, partial | 60 | 1.0 | 60 |
| **Total running** | | | **451** |

Apply a diversity factor of 0.9 for loads that are genuinely unlikely to peak together, which gives about **406 kW**. Then add growth — a hospital adds imaging, adds beds, adds air conditioning — so 20 % is a realistic allowance, giving **487 kW**. The nearest standard set is a **500 kW / 625 kVA** unit.

Then go back and check the starting case. If the chiller starts direct-on-line at six times running current while the theatre is already loaded, the set must absorb that step without dropping voltage far enough to trip medical equipment. If that check fails, the answer is not a bigger generator by default — it is a soft starter or VFD on the chiller, which is usually cheaper than 200 kW of extra alternator.

## 3. The formula, and the four corrections that matter

The base conversion is simple:

**kVA = kW ÷ power factor**

With the standard 0.8 lagging power factor used on our 50 Hz sets, 400 kW of running load needs 500 kVA of alternator — before any correction. Four corrections then apply.

**Growth allowance.** 15–25 % for a new hospital, because nobody sizes a hospital for today's bed count.

**Motor starting / step load.** The transient voltage dip should stay inside what the medical equipment tolerates. On our KC series datasheets the specified limits are a transient voltage deviation of ≤ 15 %, steady-state voltage regulation of ≤ 0.5 %, transient frequency deviation of ≤ 0.5 %, and voltage and frequency recovery within ≤ 3 seconds. Those numbers are what an ICU monitor actually experiences during a transfer.

**Site derating.** A set rated at 40 °C ambient loses capacity at 45 °C, and loses more at altitude. If the plant room runs hot because the radiator is ducted into a corner, you derate — or you fix the airflow.

**Duty.** Standby rating (limited hours, no overload capability) versus prime rating (continuous, 10 % overload for one hour). A hospital that runs the set for eight hours during a grid repair is on standby duty; a hospital in a region with daily outages is on prime duty and must be specified that way.

## 4. Two real reference points

Abstract guidance is easy to write and hard to use. These are two sets we build for hospital-duty projects, with figures taken directly from the KC technical datasheets.

| Parameter | KC-YC200 | KC-YC1600 |
|---|---|---|
| Rated / standby power | 200 kW / 220 kW | 1,600 kW / 1,760 kW |
| Voltage / current | 380/220 V, 360 A | 380/220 V, 2,880 A |
| Frequency, power factor | 50 Hz, 0.8 lagging | 50 Hz, 0.8 lagging |
| Engine | Yuchai YC6MK350L-D20, 235 kW / 258.5 kW | Yuchai YC16VTD2700-D30, 1,805 kW / 1,985 kW |
| Cylinders / displacement | In-line 6, 10.34 L, 123 × 145 mm | V16, 52.26 L, 152 × 180 mm |
| Aspiration / governor | Turbocharged intercooled, electronic | Turbocharged intercooled, electronic |
| Fuel consumption | 200 g/kWh | 200 g/kWh |
| Alternator | KCI-200, brushless, AVR, IP23, class H, copper | KCI-1600, brushless, AVR, IP23, class H, copper |
| Dimensions (L × W × H) | 3,000 × 1,100 × 1,750 mm | 5,500 × 2,200 × 2,700 mm |
| Weight | 2,800 kg | 15,800 kg (reference) |
| Noise (LP7M) | 102 dB(A) | 102 dB(A) |

**When the 200 kW class fits.** Clinics, day-surgery centres, small hospitals and imaging annexes where the essential bus is limited to theatre lighting, ICU equipment, fire systems, IT and a couple of lifts, and where the chiller stays on the normal supply. At 2,800 kg and 3 m long it can be installed in a basement plant room and moved in on a pallet truck, which matters in a retrofit where the door is 1.2 m wide.

**When the 1,600 kW class fits.** Regional and teaching hospitals where the essential bus genuinely includes central chillers, kitchens, laundry, imaging and 10–20 lifts. At 15,800 kg and 5.5 m long it needs a real plant room, a cast slab or a ground-level compound, a crane plan, and usually two sets in parallel rather than one — discussed next.

Between these two, sizes are available in steps; the point is that the datasheet should be complete enough that the consulting engineer can drop the numbers straight into the electrical model.

## 5. Fuel autonomy: the 72-hour question

Fuel is where hospital specifications most often fail an audit, because the fuel consumption figure is quoted per kWh and everyone forgets to convert it.

Take the 200 g/kWh figure and diesel at about 0.84 kg/L:

**Litres per hour = rated kW × 0.2 ÷ 0.84**

| Load (KC-YC200) | Fuel per hour | Fuel per 24 h | Fuel per 72 h |
|---|---|---|---|
| 100 % (200 kW) | 47.6 L/h | 1,143 L | 3,429 L |
| 50 % average (100 kW) | 23.8 L/h | 571 L | 1,714 L |
| 25 % average (50 kW) | 11.9 L/h | 286 L | 857 L |

So a 200 kW set carrying a realistic hospital average of about half load needs roughly **1,700 L for 72 hours**. Specify a 2,000 L main tank and you have margin plus unusable volume. For the 1,600 kW set at half load the figure is about **4,570 L per 24 hours**, which is why large hospitals get a buried or bundled bulk tank and a fuel polishing contract rather than a baseframe tank.

Three details that inspectors look for: a **day tank** sized for 8 hours of running (so a main tank problem does not immediately stop the set), **bunding at 110 %** of tank volume, and **high/low level alarms** wired to the building management system. On the fuel line itself, use a fire-rated isolation valve at the tank outlet and never route the line through a stairwell.

## 6. Redundancy, paralleling and transfer

A single generator is a single point of failure. Hospitals rarely accept that for a new build.

| Scheme | What it means | Typical use |
|---|---|---|
| N | One set sized for the essential load | Clinics, small hospitals |
| N+1 | One extra set that can carry the load if any one fails | General hospitals, 3 × 500 kW for a 1,000 kW load |
| 2N | Two complete, independent supplies with separate plant rooms | Teaching hospitals, large campuses |

Paralleling gives you more than redundancy: you can run two sets at 60 % each instead of one at 100 %, which cuts fuel burn and noise at night, and you can service one set while the other carries the load. Our controllers support load sharing, isochronous load sharing and automatic synchronising, with a bus tie so a single set can be isolated.

On transfer, the number to fix early is the changeover time. Life-safety circuits are generally expected to have power within about 10 seconds; operating theatres and ICU usually bridge that gap with UPS or a static transfer switch rather than expecting the generator to be instant. Test the whole sequence — mains fail, ATS signal, engine crank, voltage build, breaker close, load accepted — on the bench, not on the night of the outage.

## 7. Noise, siting and neighbours

The two sets in the table above are open-skid machines at 102 dB(A) measured at 7 metres on the LP7M reference point. That is loud: roughly chainsaw territory. It is acceptable inside a properly attenuated plant room or on a remote site, and unacceptable 30 metres from a ward window.

Options, in order of cost:

- **Silent canopy** — typically brings a set down to the 70–75 dB(A) at 7 m range.
- **Plant room attenuation** — acoustic lining, sealed doors, floating floor, and a correctly sized inlet and exhaust attenuator. The room is usually the cheaper way to reach a strict boundary limit on a large set.
- **Siting** — put the radiator discharge and the exhaust stack away from the ward facade, and check the stack height against the nearest openable window.

Check the local boundary limits before choosing, because they vary widely; many jurisdictions apply something in the 45–55 dB(A) range at the nearest sensitive receptor at night. Do not assume a silent canopy alone gets you there on a 1.6 MW machine — it does not.

## 8. Installation details that decide whether it works

These are the items that turn a correct datasheet into a working installation:

- **Cooling air.** The radiator needs a clear inlet and a ducted outlet to outside air. A plant room with a louvre the size of a letterbox will derate the set and cook the alternator.
- **Exhaust back pressure.** Long runs, tight bends and undersized silencers raise back pressure and cost power. Route it with the supplier's maximum allowable back pressure in hand.
- **Vibration isolation.** Spring or rubber isolators under the baseframe, plus flexible exhaust bellows and a flexible fuel connection. Without them the noise travels through the slab into the wards above.
- **Cable sizing.** Size for the set's rated current at the actual ambient, and keep generator and control cables in separate trays.
- **Earthing and neutral.** Confirm the system earthing arrangement with the hospital's electrical engineer — the generator's neutral treatment must match the installation, not the other way round.
- **Fire separation.** A generator room is a fire compartment with its own detection and, usually, its own suppression.
- **Access.** Leave the alternator end and both sides of the engine accessible; a set that cannot be serviced is a set that fails early.

## 9. Testing: the part most suppliers skip

A hospital generator is judged on the night it is needed. That is why every set leaving our Yangzhou factory goes onto a digital load bank before shipment, in a fixed sequence:

| Step | Hold | What is verified |
|---|---|---|
| No load | — | Warm-up, oil pressure, charging voltage |
| 25 % load | 30 min | Voltage and frequency stability, exhaust temperature |
| 50 % load | 30 min | Governor response, fuel consumption, noise |
| 75 % load | 60 min | Cooling system, coolant temperature, belt tension |
| 100 % load | 60 min | Full rated output, voltage regulation within ±1.5 % |
| 110 % overload | 1 min | Protection trip and alarm verification |

After the run we check insulation resistance and earth continuity following thermal cycling, verify every protection function (over-speed, high water temperature, low oil pressure, over-current, emergency stop), and test the ATS sequence end to end on the bench. A test report travels with the set.

If the project needs a witnessed test, a third-party inspection report (BV, SGS or TUV) or a site-specific FAT protocol, that has to be booked before the unit enters production — not the week before shipment.

## 10. Why hospitals work with Kaichen

We build generator sets in Yangzhou, China, from 20 kVA to 3,000 kVA, and hospital work is a significant part of what we do. Three things matter more in this segment than in any other.

**We make our own alternators.** The KCI series is wound with copper, class H insulated, IP23 protected, AVR controlled and built on the same site as the assembly line. When a hospital needs a specific transient response, we can change the alternator rather than shop for one.

**We test at full load, in-house.** A 2 MW digital load bank means a 1,600 kW set is proved at 110 % before it ships, not just at no-load in a yard.

**We document in the customer's language.** Datasheets, O&M manuals, control logic descriptions and nameplates can be supplied across the languages we publish in, which shortens commissioning when the site team is not English-speaking.

Our hospital references range from a 200 kW set for a municipal hospital to 1,600–1,800 kW class installations for regional hospital campuses, including units that have been in standby service for years with scheduled load bank tests. Every shipment carries CE and ISO 9001 documentation, a spare parts kit sized for the first service interval, and 24/7 technical support during commissioning.

## Frequently asked questions

**What size generator does a hospital need?**
It depends on the essential bus, not the bed count. A clinic with theatre lighting, ICU equipment and two lifts typically needs 150–250 kW. A 200-bed general hospital with chillers on the essential bus usually lands between 400 and 600 kW. A regional hospital campus with kitchens, laundry, imaging and 15+ lifts often needs 1,200–2,000 kW, usually as two or more sets in parallel.

**How long should hospital generator fuel last?**
Common specifications call for 72 hours at a defined load, sometimes 96 hours for critical facilities. Size the tank from the actual g/kWh figure at the expected average load — for a 200 kW set at half load, about 1,700 L covers 72 hours.

**Can a diesel generator run operating theatres?**
Yes, but not directly. The theatre is normally fed through a UPS or static transfer switch that bridges the 10–30 seconds until the generator accepts load; the generator's job is to hold voltage and frequency within the limits the medical equipment tolerates once it is on.

**Silent canopy or open set for a hospital?**
Silent for anything within earshot of patients, staff housing or a boundary. Open sets are only practical inside a properly attenuated plant room or in a remote compound.

**How often should a hospital generator be tested?**
Monthly no-load or low-load runs plus an annual full-load test on a load bank is a common baseline; many accreditation schemes require documented monthly testing and annual load testing at rated capacity. Test the ATS at the same time, not separately.

## Next step

If you are specifying a hospital set, send us the essential-bus load schedule and the site conditions — altitude, ambient temperature, boundary noise limit, fuel duration requirement — and we will size it against the actual starting case rather than a rule of thumb. You can see the class of machine we build on the [Cummins 200kW silent generator](/products/cummins-200kw-silent-diesel-generator/), the [Yuchai 300kW silent generator](/products/yuchai-300kw-silent-diesel-generator/) and the [Mitsubishi 1000kW open generator](/products/mitsubishi-1000kw-open-diesel-generator/) pages, or [contact us](/contact/) with your single-line diagram.
