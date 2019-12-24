<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:fn="http://www.w3.org/2005/xpath-functions"
    xmlns:xs="http://www.w3.org/2001/XMLSchema">
    
    <xsl:output indent="yes"/>
    
    <xsl:template match="/*:Расширение_МСЭ">
        
        <xsl:variable name="расширение_МСЭ">
            <xsl:copy-of select="json-to-xml(*:value)"/>
        </xsl:variable>
        <!-- Вывод всех value -->
        <!--<xsl:value-of select="$расширение_МСЭ//*:string/following-sibling::*:string"/>-->
        
        <xsl:for-each select="$расширение_МСЭ//*:string">
            <xsl:if test="text() = 'nationality'">
                <xsl:value-of select="following-sibling::*:string"/>
            </xsl:if>
        </xsl:for-each>
        <!--<xsl:value-of select="$расширение_МСЭ//following-sibling::*:string"/>-->
        
        
        
        <!--<xsl:for-each select="$расширение_МСЭ//*:string[text()='nationality']">
            <div style="backgroung-color: red; radius:5px;">
                
                <xsl:if test=".[@key='code']">
                    <xsl:text>код: </xsl:text>
                    <xsl:value-of select="."/>
                </xsl:if>
                <xsl:text> </xsl:text>
                <xsl:if test=".[@key='value']">
                    <xsl:text>значение: </xsl:text>
                    <xsl:value-of select="."/>
                </xsl:if>
            </div>
        </xsl:for-each>-->
        <xsl:copy-of select="$расширение_МСЭ"></xsl:copy-of>
    </xsl:template>
    
</xsl:stylesheet>
