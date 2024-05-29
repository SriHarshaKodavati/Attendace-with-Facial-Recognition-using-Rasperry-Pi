# Attendance with Facial Recognition Using Raspberry Pi

## Project Overview

This project focuses on automating the attendance system using facial recognition technology with the help of a Raspberry Pi. The primary objectives are to:

1. Automate the attendance marking process using real-time face recognition.
2. Reduce the time and errors associated with manual attendance.
3. Send automated notifications to guardians and department heads for absentees.

## Abstract

Currently, schools and other organizations use personal identification strategies such as facial recognition for attendance. Manual attendance is time-consuming and prone to errors. Our proposed solution automates the attendance system using face recognition, leveraging the Raspberry Pi and a Camera module. The system updates the attendance database in real-time and sends notifications to guardians and department heads for absentees, without any human intervention.

## Index

1. [Introduction](#introduction)
2. [Background](#background)
3. [Problem Definition](#problem-definition)
4. [Objectives](#objectives)
5. [Methodology/Procedure](#methodologyprocedure)
6. [Results and Discussion](#results-and-discussion)
7. [Conclusion and Future Scope](#conclusion-and-future-scope)
8. [References](#references)
9. [Codes in Appendix](#codes-in-appendix)

## Introduction

Face detection is a current research topic in computer vision. It involves detecting faces and storing them in a database. The facial recognition attendance system identifies individuals using facial features and marks their attendance automatically. This system is touchless and can be used for employees, students, and more, recording and storing data in real-time.

## Background

Facial recognition has been researched for over 50 years. Early systems in the 1960s used rudimentary technology to map facial features. Modern systems use advanced camera technology, machine learning, and processing speeds to accurately map and recognize faces. This technology is now widely used for automated attendance.

## Problem Definition

The problem is to develop an automated attendance system using face recognition. Manual attendance in large classrooms is tedious and time-consuming. The proposed system will automatically mark attendance by recognizing student faces using a camera and processing the images with Raspberry Pi and OpenCV.

## Objectives

- To design a face recognition-based attendance system for school events.
- To monitor student attendance during school events.
- To simplify the attendance process and reduce errors.
- To minimize the time spent on attendance management.

## Methodology/Procedure

The project involves the following steps:

1. **Raspberry Pi Implementation**: Using Raspberry Pi 3B+ with a camera module.
2. **Installing Dependencies**: Libraries required include OpenCV, NumPy, and MySQL Connector.
3. **VNC Server Installation**: For remote access and control.
4. **Database Creation**: Using PhpMyAdmin and XAMPP to store facial data.
5. **Testing Database**: Ensuring the system correctly recognizes and records attendance.

### Installation of Dependencies

```bash
pip install opencv-python numpy mysql-connector-python
