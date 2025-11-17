import svgwrite
from svgwrite.shapes import Rect, Circle

def drawSquare(PDwg: svgwrite.Drawing) -> None:
    """Prompt user for square parameters and add it to the drawing."""
    left = float(input("- Left edge position: "))
    top = float(input("- Top edge position: "))
    side = float(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Rect(insert=(left, top), size=(side, side), fill=fill, stroke=stroke))

def drawCircle(PDwg: svgwrite.Drawing) -> None:
    """Prompt user for circle parameters and add it to the drawing."""
    cx = float(input("- Center X coord: "))
    cy = float(input("- Center Y coord: "))
    r = float(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Circle(center=(cx, cy), r=r, fill=fill, stroke=stroke))

def saveSvg(PDwg: svgwrite.Drawing) -> None:
    """Prompt for filename, confirm, and save the SVG."""
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ")
    if proceed.lower() == "y":
        PDwg.save(pretty=True, indent=2)
        print("Vector saved successfully!")
    else:
        print("Save cancelled.")

import svgwrite
from svgwrite.shapes import Rect, Circle, Polygon
import math

def drawSquare(PDwg: svgwrite.Drawing) -> None:
    left = float(input("- Left edge position: "))
    top = float(input("- Top edge position: "))
    side = float(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Rect(insert=(left, top), size=(side, side), fill=fill, stroke=stroke))

def drawCircle(PDwg: svgwrite.Drawing) -> None:
    cx = float(input("- Center X coord: "))
    cy = float(input("- Center Y coord: "))
    r = float(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Circle(center=(cx, cy), r=r, fill=fill, stroke=stroke))

def drawHexagon(PDwg: svgwrite.Drawing) -> None:
    print("Insert hexagon details:")
    cx = float(input("Middle point X: "))
    cy = float(input("Middle point Y: "))
    apothem = float(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    # Calculate circumradius
    R = apothem / math.cos(math.radians(30))

    # Calculate points starting from top right, clockwise
    points = []
    for i in range(6):
        angle_deg = 30 + i * 60  # start at top right
        angle_rad = math.radians(angle_deg)
        x = cx + R * math.cos(angle_rad)
        y = cy - R * math.sin(angle_rad)  # SVG Y-axis points down
        points.append((round(x), round(y)))

    PDwg.add(Polygon(points=points, fill=fill, stroke=stroke))

def saveSvg(PDwg: svgwrite.Drawing) -> None:
    filename = input("Insert filename: ")
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ")
    if proceed.lower() == "y":
        PDwg.save(pretty=True, indent=2)
        print("Vector saved successfully!")
    else:
        print("Save cancelled.")
