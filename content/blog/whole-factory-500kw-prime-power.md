---
title: "Running a Whole Factory on One 500kW Set: How Buyers Plan It"
date: "2026-10-16"
excerpt: "A single 500kW set carrying an entire plant is a different planning problem from a backup set. Load sequencing, fuel, and redundancy decide whether the plan survives contact with the floor."
---

![A 500kW Weichai-powered silent diesel generator in a large canopy](/images/blog/blog-weichai-500kw-silent.jpg)

There is a moment in many factory projects when the buyer looks at the grid connection quote and makes a decision: either wait six months for the utility to lay a new cable and pay the connection fee, or install a diesel set that becomes the plant's main power.

When that happens, the generator stops being a backup and becomes an investment. A single 500 kW (about 625 kVA) Weichai-based silent set is a common shape for that decision. The planning, though, is different from buying a standby unit.

## Standby is not prime

The first thing to internalize: a 500 kW set bought as *prime power* is a different machine from the same box bought as standby.

- **Standby** sets sit idle 99% of the time. They run for a few hours a year. The engine is rated for that duty cycle.
- **Prime** sets run 8 to 24 hours a day. They are the main power source. The engine must be rated for continuous duty, with the right fuel system, cooling, and lubrication.

Buy a standby-rated set as prime and you will rebuild it long before you expected. Buy a prime-rated set as standby and you have spent a little more than necessary, but the machine is built for a longer life.

## Load sequencing is the whole game

A 500 kW set does not start carrying the whole factory in one second. It carries the load in a designed sequence:

1. **First 0–30 seconds:** lighting, control office, safety systems. The set warms up to rated voltage.
2. **Next minute:** smaller motors, conveyor belts, water pumps, started in staggered order by the controller.
3. **After three minutes:** large loads — air compressor, chillers, main production motors — started one by one.

Without sequencing, the first big motor start drags the voltage down and the set trips on overload. With sequencing, the factory comes up the way it would on the grid.

This is why the controller matters. A cheap three-function controller that only starts and stops is not enough for a whole-factory prime set. You need a PLC-driven controller that manages the starting sequence and sheds non-essential loads if the set runs hot.

## The fuel question

A 500 kW set burns roughly 90 to 110 liters per hour at average load. If it runs 12 hours a day, that is over a thousand liters a day.

Planning a whole-factory installation means planning fuel:

- **Day tank** on the set, 8–12 hours.
- **Bulk tank** in the yard, sized to a week of running.
- **Delivery contract** with a local diesel supplier who can reach the site on schedule.

Skipping the bulk tank is how a prime-power factory finds itself waiting for a fuel truck on a production day.

## The redundancy question

A single 500 kW set is one point of failure. For a small factory that may be acceptable: when the set is down for maintenance, production pauses. For a factory with orders to ship, buyers often plan either:

- **Two 300 kW sets in parallel**, sharing the load. When one is down, the other carries the essential load.
- **One 500 kW set plus a standby 250 kW unit**, so the critical line stays up during maintenance.

Which shape fits depends on how expensive a paused day is to the business. We price both and let the math decide.

## Weichai at this size

Weichai engines in the 400–500 kW range are common for prime-power installations because the block is simple, mechanical, and well supported across Asia and Africa. Fuel tolerance is good for local diesel quality, and the parts network is dense. For a factory in a growth market, that serviceability is what keeps production running.

## Talk to us before you spec

If you are deciding between a grid connection and a prime-power set, send us the load list, the running hours per day, and the local fuel price. We will run the numbers and show you which option actually wins over five years.
