-- ================================================
-- Template generated from Template Explorer using:
-- Create Procedure (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- This block of comments will not be included in
-- the definition of the procedure.
-- ================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE getBaseStatAvg 
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT avg(cast(HP as float)) as Hpavg, 
		avg(cast(Attack as float)) as AttackAvg,
		avg(cast(Defense as float)) as DefenseAvg,
		avg(cast(SpAttack as float)) as SpAttackAvg,
		avg(cast(SpDefense as float)) as SpDefenseAvg,
		avg(cast(Speed as float)) as SpeedAvg from dbo.pokemon2
END
GO
