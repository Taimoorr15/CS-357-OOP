# Canvas-UML
This is a UML diagram of the Canvas Programm 
1️⃣ Core Drawing Objects
Point
What it is: Represents a position (x, y) in 2D space.

Attributes:

x: float, y: float → coordinates.

Methods:

__init__ → create a point.

@property, getter, setter for x and y → encapsulation.

distance → distance to another point.

__add__, __sub__ → add or subtract points.

__str__ → convert to string.

➡ Purpose: A basic building block for all other shapes.

Line
What it is: Represents a line segment between two points.

Attributes:

start: Point

end: Point

length: float

Methods:

__init__ → create a line from start and end.

__str__ → text form of the line.

➡ Purpose: Connects two points; useful for drawing.

Pen
What it is: A drawing tool that moves to points and draws lines.

Attributes:

posFinal: Point → current position.

canvas: tkPanel → the panel it draws on.

Methods:

moveTo → move without drawing.

lineTo → draw a line to a new point.

getPos → get current position.

➡ Purpose: Bridge between drawing commands and the canvas.

tkPanel
What it is: The drawing surface.

Attributes:

height, width, length → dimensions.

lines: line[] → list of lines drawn.

Methods:

addLine(p1, p2) → adds a new line between points.

delete → clears the canvas.

draw → render everything.

➡ Purpose: Manages the visual representation of lines.

2️⃣ Turtle and App
Turtle
What it is: The moving "cursor" with a pen, similar to Python's turtle graphics.

Attributes:

angle: float → direction it faces.

pen: Pen → the pen it uses to draw.

Methods:

forward → move forward and draw.

turnRight, turnLeft → change direction.

➡ Purpose: User-controlled drawing agent.

App
What it is: Main program controller.

Attributes:

turtle: Turtle

canvas: tkPanel

Methods:

run → start the program.

➡ Purpose: Orchestrates turtle + canvas.

3️⃣ Command Pattern
This side is about making commands reusable.

Command (abstract)
Method:

execute(turtle) → generic command to do something with a turtle.

zigzagCommand & squareCommand
Both inherit from Command.

Override execute(turtle) to do specific patterns:

zigzagCommand → moves turtle in zigzag.

squareCommand → draws a square.

➡ Purpose: Separate the “what to do” from “how it’s done” — makes adding new shapes easier.

4️⃣ Relationships in the UML
Solid line with arrowhead → association (“has a”). Example: Pen has a Point and a tkPanel.

Open arrow → inheritance (“is a”). Example: zigzagCommand is a Command.

Multiplicity (e.g., lines: line[]) → collection of objects.

5️⃣ Overall Flow
App starts → creates tkPanel and Turtle.

Turtle has a Pen that draws on tkPanel.

Commands (zigzag, square, etc.) tell Turtle how to move.

Turtle’s moves get converted into lines on tkPanel.

tkPanel stores & displays the lines.

If you want, I can now draw you a mental story of how a zigzag gets from code → turtle → canvas so you fully visualize how this UML works in action. That way, it will stick permanently.

To better undertand the working of this UML, we can have a look at this example

🎬 Scene 1 — The Setup
The App is like the director of the movie.

When the movie starts (run()), the App hires:

A tkPanel (stage where drawing happens).

A Turtle (actor who moves around).

The Turtle comes with:

A Pen (its drawing tool).

The Pen is linked to the tkPanel (so it can actually draw on the stage).

🎬 Scene 2 — Choosing the Script
The App says: “Today, we’re going to perform a zigzag” → so it gives the zigzagCommand to the Turtle.

A command is basically a set of instructions written for the Turtle.

It could also give squareCommand, or any other command that implements execute(turtle).

🎬 Scene 3 — The Action
The zigzagCommand calls execute(turtle):

Turtle starts facing a certain angle (say, east).

Turtle moves forward (forward() method).

This tells the Pen: “Draw a line from my current Point to the new Point”.

Pen tells tkPanel: “Hey, store this new Line”.

tkPanel stores the line in its list (lines[]).

Turtle turns left or right (turnLeft() / turnRight()).

Moves forward again — another line gets drawn.

Repeat until the zigzag is complete.

🎬 Scene 4 — The Drawing Appears
The tkPanel now has a list of Line objects in lines[].

When draw() is called:

tkPanel looks at each Line object.

Uses each line’s start and end Points to show it visually on the screen.

🎬 The Chain of Responsibility in Code Terms
plaintext
Copy
Edit
Command (zigzag) 
    → tells Turtle 
        → tells Pen 
            → tells tkPanel 
                → stores/draws Lines 
                    → each Line has two Points
It’s like passing a message down the chain until the final drawing appears.


