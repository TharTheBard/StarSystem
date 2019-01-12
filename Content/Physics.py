import pygame
import math
import numpy

class Physics:
    def update_positions(self, systemObjects, millisecondsPassed):
        for sysObject in systemObjects:
            #Conversion: km/second -> km/frame :
            frameVelocityVector = (sysObject.velocityVector[0] / millisecondsPassed, sysObject.velocityVector[1] / millisecondsPassed)
            #Update Objects' Positions for a new frame:
            sysObject.position = (sysObject.position[0]+frameVelocityVector[0], sysObject.position[1]+frameVelocityVector[1])

    def gravity(self, systemObjects):
        for sysObject in systemObjects:
            if not sysObject.isMovable:
                continue
            self.object_velocity_update(sysObject, systemObjects)

    def object_velocity_update(self, currentObject, systemObjects):
        for sysObject in systemObjects:
            if currentObject == sysObject:
                continue
            gravAcc = self.get_grav_acc_to_object(currentObject, sysObject)
            pullVector = self.construct_pull_vector(currentObject, sysObject, gravAcc)
            self.adjust_velocity_vector(currentObject, pullVector)

    def get_grav_acc_to_object(self, pulledObject, pullingObject):
        G = 18e17
        mass = pullingObject.mass
        r = self.bodies_distance(pulledObject, pullingObject)

        return G*(mass/r**2)


    def adjust_velocity_vector(self, pulledObject, pullVector):
        pulledObject.velocityVector = (pulledObject.velocityVector[0] + pullVector[0], pulledObject.velocityVector[1] + pullVector[1])

    def construct_pull_vector(self, pulledObject, pullingObject, gravAcc):
        x = pullingObject.position[0] - pulledObject.position[0]
        y = pullingObject.position[1] - pulledObject.position[1]
        if x == 0:
            alphaRad = 1.5707963268
        else:
            alphaRad = math.atan(abs(y)/abs(x))

        aSign = numpy.sign(x)
        bSign = numpy.sign(y)

        a = math.cos(alphaRad) * gravAcc
        b = math.sin(alphaRad) * gravAcc

        return (a * aSign, b * bSign)

    def bodies_distance(self, pulledObject, pullingObject):
        return ((pullingObject.position[0] - pulledObject.position[0])**2 + (pullingObject.position[1] - pulledObject.position[1])**2)**0.5