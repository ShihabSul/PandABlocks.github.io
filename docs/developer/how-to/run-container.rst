Run in a container
==================

A PandA Development container is available from on `Github Container reistry <https://ghcr.io/pandablocks/pandablocks-dev-container>`_.



Starting the container
----------------------

To pull the container from github container registry ::

    $ docker pull https://ghcr.io/pandablocks/pandablocks-dev-container:latest

To get a released version, use a numbered release instead of ``latest``.

A directory containing all the PandA repos is required: ``REPO_DIR``.
A Vivado installation is required: ``VIVADO_DIR``.
A build directory is required: ``BUILD_DIR``

The above directories will be mounted as volumes to the container as it is run with the following command:

.. code-block:: bash

    docker run --rm -it -v REPO_DIR:/repos:Z -v /scratch/tmp/build:/build:Z -v VIVADO_DIR:/scratch/Xilinx ghcr.io/pandablocks/pandablocks-dev-container /bin/bash

In each repo you will need to:

.. code-block:: bash

    cp CONFIG.example CONFIG

.. note::

    For the Vivado installation the container path will need to match your local system. 
    i.e. if it is located in /FPGA/Xilinx you will use VIVADO_DIR:/FPGA/Xilinx 
    and you will then need to edit CONFIG as appropriate.

