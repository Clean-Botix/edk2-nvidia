# SPDX-FileCopyrightText: Copyright (c) 2021-2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# SPDX-License-Identifier: BSD-2-Clause-Patent


###############################################################################
# Stuart build for NVIDIA L4T Launcher


from pathlib import Path

from edk2nv.stuart import NVIDIASettingsManager, NVIDIAPlatformBuilder


class L4TLauncherSettingsManager(NVIDIASettingsManager):
    """SettingsManager for NVIDIA's L4T Launcher App."""

    def GetName(self):
        return "L4TLauncher"

    def GetGuid(self):
        return "be4936a8-d418-405c-9f5c-a61723884a40"

    def GetBootAppName(self):
        return "AARCH64/L4TLauncher.efi"

    def GetBootAppFile(self):
        ws_dir = Path(self.GetWorkspaceRoot())
        image_name_path = ws_dir / self.GetNvidiaConfigRoot() / "ImageName"
        platform_name = image_name_path.read_text().strip()
        target = self.GetTarget()
        return str(Path("images") / f"BOOTAA64_{platform_name}_{target}.efi")

    def GetDscName(self):
        return self.GetEdk2NvidiaDir() + "Platform/NVIDIA/L4TLauncher/L4TLauncher.dsc"

    def GetFirmwareVolume(self):
        return None


class PlatformBuilder(NVIDIAPlatformBuilder):
    """PlatformBuilder for NVIDIA's L4T Launcher."""

    SettingsManager = L4TLauncherSettingsManager
