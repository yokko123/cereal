import enum
from typing import Any

# TODO: generate from capnp files


class Car:
  class CarControl:
    class HUDControl:
      class AudibleAlert(enum.Enum):
        none = 0
        chimeEngage = 1
        chimeDisengage = 2
        chimeError = 3
        chimeWarning1 = 4
        chimeWarning2 = 5
        chimeWarningRepeat = 6
        chimePrompt = 7
        chimeWarning2Repeat = 8

      class VisualAlert(enum.Enum):
        none = 0
        fcw = 1
        steerRequired = 2
        brakePressed = 3
        wrongGear = 4
        seatbeltUnbuckled = 5
        speedTooHigh = 6
        ldw = 7

  class CarParams:
    mass: float
    rotationalInertia: float
    wheelbase: float
    centerToFront: float
    steerRatioRear: float
    tireStiffnessRear: float
    tireStiffnessFront: float
    steerRatio: float

    @staticmethod
    def from_bytes(b: bytes) -> Car.CarParams:
      pass

    class CarFw:
      pass

    class Ecu(enum.Enum):
      eps = 0
      esp = 1
      fwdRadar = 2
      fwdCamera = 3
      engine = 4
      unknown = 5
      transmission = 8  # Transmission Control Module
      srs = 9  # airbag
      gateway = 10  # can gateway
      hud = 11  # heads up display
      combinationMeter = 12  # instrument cluster

      # Toyota only
      dsu = 6
      apgs = 7

      # Honda only
      vsa = 13  # Vehicle Stability Assist
      programmedFuelInjection = 14
      electricBrakeBooster = 15
      shiftByWire = 16

    class SafetyModel(enum.Enum):
      pass

  class CarEvent:
    class EventName(enum.Enum):
      canError = 0
      steerUnavailable = 1
      brakeUnavailable = 2
      gasUnavailable = 3
      wrongGear = 4
      doorOpen = 5
      seatbeltNotLatched = 6
      espDisabled = 7
      wrongCarMode = 8
      steerTempUnavailable = 9
      reverseGear = 10
      buttonCancel = 11
      buttonEnable = 12
      pedalPressed = 13
      cruiseDisabled = 14
      radarCanError = 15
      dataNeededDEPRECATED = 16
      speedTooLow = 17
      outOfSpace = 18
      overheat = 19
      calibrationIncomplete = 20
      calibrationInvalid = 21
      controlsMismatch = 22
      pcmEnable = 23
      pcmDisable = 24
      noTarget = 25
      radarFault = 26
      modelCommIssueDEPRECATED = 27
      brakeHold = 28
      parkBrake = 29
      manualRestart = 30
      lowSpeedLockout = 31
      plannerError = 32
      ipasOverrideDEPRECATED = 33
      debugAlert = 34
      steerTempUnavailableMute = 35
      resumeRequired = 36
      preDriverDistracted = 37
      promptDriverDistracted = 38
      driverDistracted = 39
      geofenceDEPRECATED = 40
      driverMonitorOnDEPRECATED = 41
      driverMonitorOffDEPRECATED = 42
      preDriverUnresponsive = 43
      promptDriverUnresponsive = 44
      driverUnresponsive = 45
      belowSteerSpeed = 46
      calibrationProgressDEPRECATED = 47
      lowBattery = 48
      invalidGiraffeHondaDEPRECATED = 49
      vehicleModelInvalid = 50
      controlsFailed = 51
      sensorDataInvalid = 52
      commIssue = 53
      tooDistracted = 54
      posenetInvalid = 55
      soundsUnavailable = 56
      preLaneChangeLeft = 57
      preLaneChangeRight = 58
      laneChange = 59
      invalidGiraffeToyota = 60
      internetConnectivityNeeded = 61
      communityFeatureDisallowed = 62
      lowMemory = 63
      stockAeb = 64
      ldw = 65
      carUnrecognized = 66
      radarCommIssue = 67
      driverMonitorLowAcc = 68
      invalidLkasSetting = 69
      speedTooHigh = 70
      laneChangeBlockedDEPRECATED = 71
      relayMalfunction = 72
      gasPressed = 73
      stockFcw = 74
      startup = 75
      startupNoCar = 76
      startupNoControl = 77
      startupMaster = 78
      fcw = 79
      steerSaturated = 80
      whitePandaUnsupported = 81
      startupWhitePanda = 82
      canErrorPersistent = 83
      belowEngageSpeed = 84

  class CarState:
    class GearShifter(enum.Enum):
      unknown = 0
      park = 1
      drive = 2
      neutral = 3
      reverse = 4
      sport = 5
      low = 6
      brake = 7
      eco = 8
      manumatic = 9

    class ButtonEvent:
      class Type(enum.Enum):
        unknown = 0
        leftBlinker = 1

        accelCruise = 3
        decelCruise = 4
        cancel = 5
        altButton1 = 6
        altButton2 = 7
        altButton3 = 8
        setCruise = 9
        resumeCruise = 10
        gapAdjustCruise = 11

car: Car
log: Any
