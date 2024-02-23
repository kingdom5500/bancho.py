from __future__ import annotations

from typing import Any


def vivid_osu_file_sample_response() -> bytes:
    with open("testing/sample_data/vivid_osu_file.osu", "rb") as f:
        return f.read()


def vivid_getbeatmaps_sample_response() -> list[dict[str, Any]]:
    return [
        {
            "beatmapset_id": 141,
            "beatmap_id": 313,
            "approved": 1,
            "total_length": 188,
            "hit_length": 159,
            "version": "Easy",
            "file_md5": "72bdc73c3f17013c5d0ba8443c9045b2",
            "diff_size": 3,
            "diff_overall": 3,
            "diff_approach": 3,
            "diff_drain": 3,
            "mode": 0,
            "approved_date": "2007-11-01T06:09:15Z",
            "last_update": "2014-05-18T08:16:40Z",
            "artist": "FAIRY FORE",
            "artist_unicode": "FAIRY FORE",
            "title": "Vivid",
            "title_unicode": "Vivid",
            "creator": "Hitoshirenu Shourai",
            "creator_id": 602,
            "bpm": 168,
            "source": "",
            "tags": "",
            "genre_id": 0,
            "language_id": 0,
            "favourite_count": 336,
            "storyboard": 0,
            "video": 0,
            "download_unavailable": 0,
            "playcount": 53584,
            "passcount": 15160,
            "packs": ["S5", "T79"],
            "max_combo": 294,
            "difficultyrating": 1.54,
        },
        {
            "beatmapset_id": 141,
            "beatmap_id": 314,
            "approved": 1,
            "total_length": 185,
            "hit_length": 182,
            "version": "Hard",
            "file_md5": "dd1749b4422a1dab9a2945a6bfccc5ef",
            "diff_size": 5,
            "diff_overall": 5,
            "diff_approach": 5,
            "diff_drain": 5,
            "mode": 0,
            "approved_date": "2007-11-01T06:09:15Z",
            "last_update": "2014-05-18T16:45:16Z",
            "artist": "FAIRY FORE",
            "artist_unicode": "FAIRY FORE",
            "title": "Vivid",
            "title_unicode": "Vivid",
            "creator": "Hitoshirenu Shourai",
            "creator_id": 602,
            "bpm": 168,
            "source": "",
            "tags": "",
            "genre_id": 0,
            "language_id": 0,
            "favourite_count": 336,
            "storyboard": 0,
            "video": 0,
            "download_unavailable": 0,
            "playcount": 79331,
            "passcount": 8523,
            "packs": ["S5", "T79"],
            "max_combo": 723,
            "difficultyrating": 3.75,
        },
        {
            "beatmapset_id": 141,
            "beatmap_id": 315,
            "approved": 1,
            "total_length": 14,
            "hit_length": 14,
            "version": "Insane",
            "file_md5": "1cf5b2c2edfafd055536d2cefcb89c0e",
            "diff_size": 6,
            "diff_overall": 7,
            "diff_approach": 7,
            "diff_drain": 2,
            "mode": 0,
            "approved_date": "2007-11-01T06:09:15Z",
            "last_update": "2014-05-18T15:41:48Z",
            "artist": "FAIRY FORE",
            "artist_unicode": "FAIRY FORE",
            "title": "Vivid",
            "title_unicode": "Vivid",
            "creator": "Hitoshirenu Shourai",
            "creator_id": 602,
            "bpm": 168,
            "source": "",
            "tags": "",
            "genre_id": 0,
            "language_id": 0,
            "favourite_count": 336,
            "storyboard": 0,
            "video": 0,
            "download_unavailable": 0,
            "playcount": 1632137,
            "passcount": 987366,
            "packs": ["S5", "T79"],
            "max_combo": 114,
            "difficultyrating": 5.23,
        },
        {
            "beatmapset_id": 141,
            "beatmap_id": 316,
            "approved": 1,
            "total_length": 188,
            "hit_length": 159,
            "version": "Normal",
            "file_md5": "0236aeb3bb5f110d7eacf4045092efac",
            "diff_size": 5,
            "diff_overall": 5,
            "diff_approach": 5,
            "diff_drain": 5,
            "mode": 0,
            "approved_date": "2007-11-01T06:09:15Z",
            "last_update": "2014-05-18T16:26:49Z",
            "artist": "FAIRY FORE",
            "artist_unicode": "FAIRY FORE",
            "title": "Vivid",
            "title_unicode": "Vivid",
            "creator": "Hitoshirenu Shourai",
            "creator_id": 602,
            "bpm": 168,
            "source": "",
            "tags": "",
            "genre_id": 0,
            "language_id": 0,
            "favourite_count": 336,
            "storyboard": 0,
            "video": 0,
            "download_unavailable": 0,
            "playcount": 49671,
            "passcount": 13422,
            "packs": ["S5", "T79"],
            "max_combo": 478,
            "difficultyrating": 2.28,
        },
    ]
