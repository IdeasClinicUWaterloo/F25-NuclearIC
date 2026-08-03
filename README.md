# CNL Nuclear Waste Transport Monitoring Challenge

Welcome! This document describes the challenge, background, and sub-problems for the CNL Nuclear Waste Transport Monitoring project.

## Table of Contents

1. [Introduction](#introduction)
2. [Your Mission](#your-mission)
3. [Sub-Problem 1: Vehicle State Monitoring](#sub-problem-1-vehicle-state-monitoring)
4. [Sub-Problem 2: Environmental Challenges and Route Planning](#sub-problem-2-environmental-challenges-and-route-planning)
5. [Sub-Problem 3: Loading and Unloading](#sub-problem-3-loading-and-unloading)
6. [Sub-Problem 4: Alerts and Communication](#sub-problem-4-alerts-and-communication)
7. [Reference Documents and Links](#reference-documents-and-links)

---

## Introduction

Canada is building a **nuclear waste repository** in Ignace, Ontario, to safely contain spent nuclear fuel produced by **CANDU reactors** across the country. Once operational, the facility will receive nuclear waste transported thousands of kilometres by road from nuclear power plants nationwide.

The **Canadian Nuclear Safety Commission (CNSC)** regulates this project because of the significant safety risks involved. A vehicle or storage failure could cause serious environmental or human exposure. A robust **monitoring system** is therefore needed to:

- Detect radiation exposure
- Protect against anyone attempting to misuse the nuclear waste

Trucks will carry radioactive material through populated cities, along highways, and through unpredictable weather — each presenting its own sensing challenges. CNSC's role is to regulate the transport and handling of nuclear substances in order to protect:

- The **safety and health** of the public
- The **workers** in the nuclear sector
- The **environment**

**Watch:** [Background video on the project](https://www.youtube.com/watch_popup?v=DTEPPzmhYks) (opens on YouTube)

---

## Your Mission

Your team at CNL has been tasked with designing the **monitoring systems** used to track nuclear waste during transport. Working as an interdisciplinary team, you will develop a solution to one or more sub-problems below. Prior teams have already reviewed radiation monitoring, sensor technology, and system integration, and their groundwork and resources are linked throughout this document.

**The four sub-problems are:**

1. Live vehicle state monitoring during transport
2. Route planning and response to environmental challenges (fires, potholes, snow, floods, accidents, fuel shortages, etc.)
3. Safe loading and unloading along the route
4. Communication technology for emergency response

You may address one sub-problem in depth, or find a creative way to combine solutions across multiple areas.

**Timeline reminder:** Top scientists at CNL will arrive **in two days** to assess your results, so work efficiently.

Please work pragmatically and safely throughout the challenge. For additional background, see the [Nuclear Transport Q&A document](https://github.com/IdeasClinicUWaterloo/F25-NuclearIC/blob/main/nuclear_transport_Q_and_As.pdf) (PDF).

---

## Sub-Problem 1: Vehicle State Monitoring

Trucks will travel from all four participating provinces to the deposition site in Ignace, carrying spent fuel to the deep repository. Along the way, they will pass through a range of environments and weather conditions that can affect the vehicle, including:

- **Vibrations** on uneven ground, which increase the risk of containers or fastenings coming loose
- **Rain**, which reduces visibility and creates slippery road conditions
- **Tire quality**, which impacts safe transport
- **Loading and unloading** into different vehicles, which may shift weight distribution and cause instability

Spent fuel is transported in heavily shielded casks. Radiation is difficult to detect from outside the cask, but if the shielding is compromised, **radiation leakage** becomes possible.

### The Challenge

For this exercise, an **infrared (IR) emitter** stands in for real radiation. Your task is to design a system that improves **planning, monitoring, or reacting** to changes in vehicle and container condition.

**Resource:** [Sensor Package Sub-problem materials](https://github.com/IdeasClinicUWaterloo/F25-NuclearIC/tree/main/Sensor%20Package%20Subproblem) — covers methods for implementing sensors and tools to accurately gauge the condition of the transport truck.

---

## Sub-Problem 2: Environmental Challenges and Route Planning

Transport happens year-round across four provinces — Ontario, Manitoba, Quebec, and New Brunswick — so trucks may face a variety of environmental hazards, such as:

- A **forest fire** in southeastern Manitoba, causing debris, smoke, and obstacles
- **Flooding** in Northern Ontario, affecting the Trans-Canada Highway (often the only available route)
- **Snow and icy conditions** during winter months

### The Challenge

Design a system that optimizes truck routing based on environmental hazards and on-route resources (for example, gas stations).

**Resource:** [Route Optimization Sub-problem materials](https://github.com/IdeasClinicUWaterloo/F25-NuclearIC/tree/main/Route_Optimization_Subproblem) — the example solution builds a map and plans the most efficient route from several nuclear sites (marked in blue) to the planned repository location (marked in violet). It accounts for environmental obstacles and weather events — such as a forest fire along the initial route (marked in red) — that could make a route less desirable.

---

## Sub-Problem 3: Loading and Unloading

Continuous monitoring of nuclear materials at every stage of transport is essential to protect the materials themselves, the environment, and the people involved.

During transit, the transport **flask must sometimes be loaded and unloaded** from trucks. This process requires close monitoring to keep employees safe. Even with strict protocols and layered safety measures in place, incidents such as **material spills, equipment malfunctions, or accidental drops** can still occur. There is also a risk that **unauthorized personnel** could attempt to access the material during transport, raising the risk of tampering or interference.

CNSC wants to strengthen safety surveillance during loading and unloading. Possible approaches include a monitoring system, safer methods for handling the container cask, or alternative designs that reduce risk overall.

### The Challenge

Design a system that enables a **safe nuclear transfer process**, minimizing the risk of exposure, material tampering, and unauthorized access to the transfer site.

**Resource:** [Loading and Unloading Sub-problem materials](https://github.com/IdeasClinicUWaterloo/F25-NuclearIC/tree/main/Loading_Unloading_Subproblem) — the example solution uses open-source computer vision to monitor the transfer site and confirm it is safe and free of unauthorized personnel.

---

## Sub-Problem 4: Alerts and Communication

In an emergency, timely alerts must reach both authorities and the public. Authorities need a comprehensive overview of the situation so they can prepare an appropriate response, while the public needs clear warnings about threats and the safety measures to follow.

This requires a system that can turn raw vehicle state data into actionable information and communicate it effectively — with attention to tone, audience, and channel. Communication may need to happen across multiple channels, such as social media and an internal real-time dashboard.

### The Challenge

Create a system that improves communication with authorities, administrators, and the public during an emergency.

**Resource:** [Communication Sub-problem materials](https://github.com/IdeasClinicUWaterloo/F25-NuclearIC/tree/main/Communication_Subproblem) — the example solution includes a public dashboard and a Bluesky alert bot.

---

## Reference Documents and Links

- [Judging rubric, presentation template, and group signups (Google Drive folder)](https://drive.google.com/drive/folders/1HSpPK-RUN6NwezttZxGLrhhvPRYHUJKT?usp=sharing)
- [Background video on the project](https://www.youtube.com/watch_popup?v=DTEPPzmhYks)
- [Nuclear Transport Q&A document (PDF)](https://github.com/IdeasClinicUWaterloo/F25-NuclearIC/blob/main/nuclear_transport_Q_and_As.pdf)
- [Sensor Package Sub-problem materials](https://github.com/IdeasClinicUWaterloo/F25-NuclearIC/tree/main/Sensor%20Package%20Subproblem)
- [Route Optimization Sub-problem materials](https://github.com/IdeasClinicUWaterloo/F25-NuclearIC/tree/main/Route_Optimization_Subproblem)
- [Loading and Unloading Sub-problem materials](https://github.com/IdeasClinicUWaterloo/F25-NuclearIC/tree/main/Loading_Unloading_Subproblem)
- [Communication Sub-problem materials](https://github.com/IdeasClinicUWaterloo/F25-NuclearIC/tree/main/Communication_Subproblem)

Good luck and have fun!
