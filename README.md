A development with **AIDE** has two parts:

- One were the activities of daily living, the actors involved, the physical realm, and the elements in the AmI are defined.
- Another were the control software for AmI elements are created. This control software can be developed as a prototype or a production solution. The prototypes can be modeled using the SociAALML language or programmed in Python. SociAALML prototypes are generated as part of the simulation. While Python prototypes run outside of the simulation and interacts with it thanks to a JSON API. The platform supported for production is Android. Using a library called jALI, Android solutions are able to interact with the simulated environment.

This project is focused on modeling situations and their prototyped approaches.

The project is organized as follow:
- **common-task-model:** It contains a set of basic parameterized activities of daily living modeled with SociAALML. Its aims is to be a repository to reuse these models in specific domains.
- **alzheimer-model:** A SociAALML model of Alzheimer's Patient undesired situations and prototypes of their solutions.
- **ami-prototypes:** Prototypes of AmI solutions coded in Python. They can check the state of the simulation entities and change them. For example, switching a light off if nobody is in the room, or firing an alarm if the patient falls.

# REQUIREMENTS:

Basic development requires the following:

- Java 1.7 (set variable JAVA_HOME)
- Maven 3.1.1+ installed, see http://maven.apache.org/download.html (set variable M2_HOME)
- Ant (set variable ANT_HOME)
- Python

# GENERAL USAGE:

There are specific instructions for each scenario. However, the process is pretty similar for all of them.

1. to install the dependencies:
```
mvn clean install
```
2. to open the sociAALML editor:
```
ant edit
```

3. Once the changes are done and saved, to generate de code:
```
ant compile
```

4. To run a simulation diagram (e.g. MySimulation).
```
ant runMySimulation [-Dml=true] [-Drecord=true]
```
-Dml=true and -Dml=record are opcional parameters. The firs one is necessary if the simulation requires to process audio (e.g. charecters listen each other). The second one will generate a video of the simulation called PHAT-MySimulation.mp4.

5. If the AmI prototype is coded in Python, once the simulation is running, it's time to start the script:
```
python scriptName.py
```
