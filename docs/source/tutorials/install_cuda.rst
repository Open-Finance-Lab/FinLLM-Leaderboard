=============
Install Cuda
=============

.. contents:: Table of Contents
   :local:

Install CUDA Toolkit
====================

.. note::
   This section is only required if you're **running LLMs locally** on your physical machine.

   For Google Colab users:

   - Skip this installation (Colab provides pre-installed CUDA environments)

   - Proceed directly to :doc:`/basics_setup/get_api_keys`


Install Cuda
--------------------

1. **Cuda Install**

   Determine which version of cuda you should download

   In the terminal, type

   .. code-block:: bash

      nvidia-smi   //This will give information of your graphics driver
      // Find this line
      +-----------------------------------------------------------------------------------------+
      | NVIDIA-SMI 566.36                 Driver Version: 566.36         CUDA Version: 12.8     |
      |-----------------------------------------+------------------------+----------------------+

   The following guide will use CUDA 12.8 as an example

   a. Visit `CUDA Toolkit Archive <https://developer.nvidia.com/cuda-toolkit-archive>`_
   b. Select version matching your framework requirements:

    .. image:: /basics_setup/images/Archive.png
       :align: center
       :class: custom-img

   c. Follow the installation instruction and choose default setups

   .. code-block:: bash

      // Verify installations
      nvcc -v


2. **cuDNN Version**
   a. Visit `cuDNN Toolkit Archive <https://developer.nvidia.com/rdp/cudnn-archive>`_

   Download
    .. image:: /basics_setup/images/cudnn_archive.png
       :align: center
       :class: custom-img

    .. image:: /basics_setup/images/cudnn_zip.png
       :align: center
       :class: custom-img

    **Unzip everything from cuDNN zip to your local CUDA directory**

    .. image:: /basics_setup/images/cudnn_files.png
       :align: center
       :class: custom-img

    **Create Environment Variables**

    .. image:: /basics_setup/images/env_var.png
       :align: center
       :class: custom-img


   .. code-block:: bash

      C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8\bin
      C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8\lib
      C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8\include
      C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8\libnvvp

