Migration Guide
===============

The following is information key to migrating from one version of the PandA firmware to another.

To change PandA firmware, follow the steps outlined here :ref:`ssh_doc`.

2.0 to 3.0
==========

Changelogs:

================== ==================================================================
PandABlocks-FPGA   https://github.com/PandABlocks/PandABlocks-FPGA/releases/tag/3.0
PandABlocks-Server https://github.com/PandABlocks/PandABlocks-server/releases/tag/3.0
PandABlocks-rootfs https://github.com/PandABlocks/PandABlocks-rootfs/releases/tag/3.0
================== ==================================================================

API changes:

============== =======================================================================
Block          Change
============== =======================================================================
Calc           removed fields: Func
Clock          new fields: Width, WidthUnits
Counter        new field: outMode, trigEdge
Inenc          new field: encoding
Outenc         new field: encoding
Pcap           changed field: sample -> gateDuration
Seq            new fields: health, canWriteNext
SFP DLS_Eventr new field: cpllLock
SFP PandA_Sync new fields: in.health, in.ERR_cnt
|              removed fields: BIT9, BIT10, BIT11, BIT12, BIT13, BIT14, BIT15, BIT16
System         new field: ext_clock_freq
|              changed field: extClock -> clocksource
============== =======================================================================
